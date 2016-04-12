Array.prototype.shuffle = function() {
  var curindex = this.length, random_index;
  while (curindex) {
    random_index = (Math.random() * curindex--) | 0;
    [this[curindex], this[random_index]] = [this[random_index], this[curindex]]
  }
  return this;
}

function createTiles(n){
  // TODO: Return array of bricks
  if(n<=0 || n%2 == 1){
    return [];
  }
  var ret = [];
  for(i=1; i<=n/2; i++){
    ret.push(i);
    ret.push(i);
  }
  return ret.shuffle();
}