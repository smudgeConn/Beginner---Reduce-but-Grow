export function breakCamelCase(input) {
  let res = "";
  const len = input.length;
  if (len > 0) {
    for (let i = 0; i < len; i++) {
      const char = input[i];
      if (char === char.toLowerCase()) {
        res += char;
      } else {
        res += " " + char;
      }
    }
    return res;
  } else {
    return input;
  }
}
