#!/usr/bin/yarn dev
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
  const text = 'Redis client connected to the server';
  console.log(text);
});

client.on('error', (err) => {
  const text = 'Redis client not connected to the server:';
  console.log(text, err.toString());
});
