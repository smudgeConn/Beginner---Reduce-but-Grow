function printerError(s) {
  
  let colors = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'];
  
  let denominator = s.length;
  
  let numerator = 0;
  
  for (let i = 0; i < denominator; i++) {
    if (colors.includes(s[i]) == false) {
      numerator += 1;
    }
  }
 return numerator.toString() + "/" + denominator.toString(); 
}
