import { test } from "node:test";
import assert from "node:assert/strict";
import { greet, farewell } from "../src/greet.js";

test("greets a given name", () => {
  assert.equal(greet("World"), "Hello, World!");
});

test("rejects an empty name", () => {
  assert.throws(() => greet(""), TypeError);
});

test("farewells a given name", () => {
  assert.equal(farewell("World"), "Goodbye, World!");
});

test("farewell preserves the name as supplied (no trimming)", () => {
  assert.equal(farewell("  alice  "), "Goodbye,   alice  !");
});

test("farewell rejects an empty name", () => {
  assert.throws(() => farewell(""), TypeError);
});

test("farewell rejects an undefined name", () => {
  assert.throws(() => farewell(undefined), TypeError);
});

test("farewell rejects non-string names", () => {
  for (const bad of [null, 42, {}, true]) {
    assert.throws(() => farewell(bad), TypeError);
  }
});

test("farewell throws with the documented message", () => {
  assert.throws(
    () => farewell(""),
    (err) =>
      err instanceof TypeError &&
      err.message === "farewell(name) requires a non-empty string",
  );
});
