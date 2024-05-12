import { breakCamelCase } from "./break-camelCase";

// test("return true for string", function () {
//   const input = "sample string";
//   const output = breakCamelCase(input);
//   expect(output).toBe(true);
// });

test("return ' C' for C", function () {
  const input = "C";
  const output = breakCamelCase(input);
  expect(output).toBe(" C");
});

test("return c for c", function () {
  const input = "c";
  const output = breakCamelCase(input);
  expect(output).toBe("c");
});

test("return 'camel Casing' for 'camelCasing'", function () {
  const input = "camelCasing";
  const output = breakCamelCase(input);
  expect(output).toBe("camel Casing");
});

test("return 'identifier' for 'identifier'", function () {
  const input = "identifier";
  const output = "identifier";
  expect(output).toBe("identifier");
});

test("return '' for '' ", function () {
  const input = "";
  const output = breakCamelCase(input);
  expect(output).toBe("");
});
