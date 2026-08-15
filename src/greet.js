export function greet(name) {
  if (!name || typeof name !== "string") {
    throw new TypeError("greet(name) requires a non-empty string");
  }
  return `Hello, ${name}!`;
}
