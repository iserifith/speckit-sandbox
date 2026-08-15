export function greet(name) {
  if (!name || typeof name !== "string") {
    throw new TypeError("greet(name) requires a non-empty string");
  }
  return `Hello, ${name}!`;
}

export function farewell(name) {
  if (!name || typeof name !== "string") {
    throw new TypeError("farewell(name) requires a non-empty string");
  }
  return `Goodbye, ${name}!`;
}
