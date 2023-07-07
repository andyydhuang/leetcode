/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let output = [];

    var flat_func = function(array, dimen) {
      /*
      console.log('------------')
      console.log(`dimen ${dimen}`)
      console.log(array);
      */
      if (dimen === n) {
        output.push(array);
        return;
      }

      for (let i = 0 ; i < array.length; i++) {  
        if (Array.isArray(array[i]) === false)
            output.push(array[i]);
        else {
            flat_func(array[i], dimen+1)
        }
      }
    }

    flat_func(arr, -1);
    return output;
};