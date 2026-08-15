import { test } from "node:test";
import assert from "node:assert/strict";
import { greet, shout } from "../src/greet.js";

test("greets a given name", () => {
  assert.equal(greet("World"), "Hello, World!");
});

test("rejects an empty name", () => {
  assert.throws(() => greet(""), TypeError);
});

test("shout returns the name in all caps", () => {
  assert.equal(shout("alice"), "ALICE");
  assert.equal(shout("AlIcE"), "ALICE");
  assert.equal(shout("BOB"), "BOB");
  assert.equal(shout("alice 42!"), "ALICE 42!");
});

test("shout passes the empty string through unchanged", () => {
  assert.equal(shout(""), "");
});

test("shout passes whitespace-only strings through unchanged", () => {
  assert.equal(shout("   "), "   ");
});

test("shout rejects non-string input with TypeError", () => {
  for (const value of [undefined, null, 42, {}, true, Symbol("x"), 10n]) {
    assert.throws(() => shout(value), TypeError);
  }
});
