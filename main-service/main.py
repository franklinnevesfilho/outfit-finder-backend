from franklin_fastapi_extension import API, Query
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from logger import logger
import httpx
import os

app = API()

# Define the base URLs for your microservices
services = {
    "auth": os.getenv("AUTH_SERVICE_URL", None),
}


# Generic forwarding function
async def forward_request(service_url: str, path:str, request: Query):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}/{path}"
        headers = request.headers
        params = request.query_params

        # Forward request based on the method
        if request.method == "GET":
            response = await client.get(url, headers=headers, params=params)
        elif request.method == "POST":
            response = await client.post(url, headers=headers, content=await request.body())
        elif request.method == "PUT":
            response = await client.put(url, headers=headers, content=await request.body())
        elif request.method == "DELETE":
            response = await client.delete(url, headers=headers, params=params)
        else:
            raise HTTPException(status_code=405, detail="Method not allowed")

        return response


# Route traffic based on the endpoint prefix
@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, path: str, request: Query):
    service_url = services.get(service)
    if not service_url:
        raise HTTPException(status_code=404, detail="Service not found")

    logger.info(f"Forwarding request to {service_url}/{path}")
    # Forward the request to the appropriate service
    response = await forward_request(service_url, path, request)

    try:
        # Attempt to parse the response content as JSON
        content = response.json()
        return JSONResponse(content=content, status_code=response.status_code, headers=dict(response.headers))
    except ValueError:
        # If the response is not JSON, return it as-is
        return response.content, response.status_code, response.headers.items()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
