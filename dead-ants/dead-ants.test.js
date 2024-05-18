import { deadAnts } from "./dead-ants";
test("return 0 for ant", function () {
  const input = "ant";
  const output = deadAnts(input);
  expect(output).toBe(0);
});

test("return 1 for nat", function () {
  const input = "nat";
  const output = deadAnts(input);
  expect(output).toBe(1);
});

test("return 0 for antant", function () {
  const input = "antant";
  const output = deadAnts(input);
  expect(output).toBe(0);
});

test("return 0 for ant.ant", function () {
  const input = "antant";
  const output = deadAnts(input);
  expect(output).toBe(0);
});

test("return 1 for anant", function () {
  const input = "anant";
  const output = deadAnts(input);
  expect(output).toBe(1);
});

test("return 2 for an.ta.nt", function () {
  const input = "an.ta.nt";
  const output = deadAnts(input);
  expect(output).toBe(2);
});
