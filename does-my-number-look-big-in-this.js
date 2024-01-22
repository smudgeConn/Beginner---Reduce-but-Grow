function narcissistic(value) {
  length = value.toString().length;
  let sum = 0;
  
  for (let i = 0; i < length; i++) { 
    sum += parseInt(value.toString()[i])**length;
  }
  
  return sum == value ? true : false  
}
