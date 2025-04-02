CREATE EXTENSION IF NOT EXISTS vector;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create sample table for storing items with vector embeddings
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    item_data JSONB,
    embedding vector(1536)  -- Adjust dimension as necessary
);

CREATE TABLE IF NOT EXISTS categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(120) NOT NULL,
    description VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Create Product table
CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(120) NOT NULL,
    description VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Create Product table
CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(120) NOT NULL,
    description VARCHAR(500),
    price FLOAT NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    status VARCHAR(20) NOT NULL CHECK (status IN ('Available', 'Not Available')),
    image BYTEA,
    category_id UUID REFERENCES categories(id) ON DELETE CASCADE
);

-- Insert initial categories
INSERT INTO categories (id, name, description) VALUES
('07ea2615-096b-42de-9849-dfd18875fb55', 'Clothing', 'Apparel and garments'),
('c329a254-6462-4e82-ad26-9c976f0bb11f', 'Footwear', 'Shoes and boots'),
('5240caa0-7b87-4b86-8104-c22047d36ec5', 'Accessories', 'Fashion accessories and small goods'),
('497446b9-19bc-4c18-a3de-1e42b4180df1', 'Bags', 'Backpacks and carrying accessories');

-- Insert initial products
INSERT INTO products (id, name, description, price, stock, status, category_id) VALUES
('1e6e2d61-1f6a-4f5a-bb7f-8a5d3b6e6a84', 'Classic T-Shirt', 'Comfortable cotton t-shirt in various colors', 1649.17, 10, 'Available', '07ea2615-096b-42de-9849-dfd18875fb55'),
('c9f3c2b2-d2d8-4f7e-bd92-fc8c5f1eb7b1', 'Running Shoes', 'Lightweight athletic shoes for running', 7424.17, 10, 'Available', 'c329a254-6462-4e82-ad26-9c976f0bb11f'),
('3ee1c6d3-b7e8-4f8a-a5a0-f95d0cd9b3e7', 'Leather Wallet', 'Genuine leather bifold wallet', 2474.17, 0, 'Not Available', '5240caa0-7b87-4b86-8104-c22047d36ec5'),
('6ab5d2aa-b0ff-48a8-b7cc-e30bf6a6e8be', 'Backpack', 'Durable waterproof backpack for everyday use', 4124.17, 10, 'Available', '497446b9-19bc-4c18-a3de-1e42b4180df1'),
('bdbaf5d5-f7e3-44ed-b43d-de13a64fc678', 'Sunglasses', 'UV protection sunglasses with polarized lenses', 6599.17, 10, 'Available', '5240caa0-7b87-4b86-8104-c22047d36ec5');