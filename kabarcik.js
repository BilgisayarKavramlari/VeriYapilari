var dizi = [2,3,6,3,4,1,9,8,2,6];

function kabarcikSirala(d) {
  var dondu;
  do {
    dondu = false;
    for(var i=0; i < d.length-1; i++)
      if(d[i] > d[i+1]) {
        var gecici = d[i];
        d[i] = d[i+1];
        d[i+1] = gecici;
        dondu = true;
      }
  } while (dondu);
}

kabarcikSirala(dizi);

console.log(dizi);
