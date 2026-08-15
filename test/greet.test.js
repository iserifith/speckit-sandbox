import { test } from "node:test";
import assert from "node:assert/strict";
import { greet } from "../src/greet.js";

test("greets a given name", () => {
  assert.equal(greet("World"), "Hello, World!");
});

test("rejects an empty name", () => {
  assert.throws(() => greet(""), TypeError);
});
