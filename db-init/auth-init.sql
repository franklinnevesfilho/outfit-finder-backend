CREATE DATABASE IF NOT EXISTS auth_service;

USE auth_service;

CREATE TABLE IF NOT EXISTS users (
    id char(36) PRIMARY KEY,
    profile_img VARCHAR(255),
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS roles (
    id char(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS user_settings (
    id char(36) PRIMARY KEY,
    user_id char(36) NOT NULL,
    role_id char(36) NOT NULL,
    2fa_enabled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);