export function deadAnts(ants) {
  console.log(ants);
  if (ants === null) {
    return 0;
  }
  let numOfSurvivors = 0;
  let letterLength = ants.length;
  let antLength = ants.length - 2;
  let numNs = 0;
  let numTs = 0;
  let numAs = 0;

  for (let i = 0; i < letterLength; i++) {
    let letter = ants[i];
    if (letter === "a") {
      numAs++;
    }
    if (letter === "n") {
      numNs++;
    }
    if (letter === "t") {
      numTs++;
    }
  }
  let total = Math.max(numAs, numNs, numTs);

  for (let i = 0; i < antLength; i++) {
    let letter = ants[i];
    let nextLetter = ants[i + 1];
    let thirdLetter = ants[i + 2];
    if (letter + nextLetter + thirdLetter === "ant") {
      numOfSurvivors++;
    }
  }
  return total - numOfSurvivors;
}
