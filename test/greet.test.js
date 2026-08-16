import { test } from "node:test";
import assert from "node:assert/strict";
import { greet, shout } from "../src/greet.js";

test("greets a given name", () => {
  assert.equal(greet("World"), "Hello, World!");
});

test("rejects an empty name", () => {
  assert.throws(() => greet(""), TypeError);
});

test("shouts a lowercase name in caps", () => {
  assert.equal(shout("alice"), "ALICE");
});

test("shouts an empty string to empty string", () => {
  assert.equal(shout(""), "");
});

test("shouts rejects non-string input", () => {
  assert.throws(() => shout(42), TypeError);
  assert.throws(() => shout(null), TypeError);
  assert.throws(() => shout(undefined), TypeError);
});
