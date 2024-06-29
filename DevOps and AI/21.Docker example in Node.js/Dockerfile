# Use official Node.js image
FROM node:latest

# Create app directory
WORKDIR /usr/src/app

# Copy package.json and yarn.lock to container
COPY package*.json ./

# Install app dependencies using yarn
RUN yarn install

# Copy the rest of the application source code
COPY . .

# Set the working directory to src
WORKDIR /usr/src/app/src

# Expose the port the app runs on
EXPOSE 3000

# Command to run the app
CMD ["node", "index.js"]
