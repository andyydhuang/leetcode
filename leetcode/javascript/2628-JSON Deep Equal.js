/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) { 
  return customJsonStringify(o1, o2)
};


/**
 * @param {any} object
 * @return {string}
 */
var customJsonStringify = function(obj1, obj2) {
  let buff = []

  var handle_object_function = function(val1, key1, val2, key2) {
    let o1_type = typeof val1
    let o2_type = typeof val2

    if (o1_type != o2_type) {
      buff.push(false);
      return; 
    }
    //Both Primitive
    if (o1_type !== 'object') {
      if (val1 !== val2) {
        buff.push(false);       
      }
      return;
    }

    o1_is_null = val1 === null;
    o2_is_null = val2 === null;
    let null_case = o1_is_null + o2_is_null
    if (null_case === 1) {
      buff.push(false);
      return; 
    }
    else if (null_case === 2)
      return 

    o1_is_array = Array.isArray(val1);
    o2_is_array = Array.isArray(val2);

    let array_case = o1_is_array + o2_is_array
    if (array_case === 1) {
      buff.push(false);
      return;
    }

      if (array_case === 2) {
        if (val1.length !== val2.length) {
          buff.push(false);
          return;
        }
        for (let index = 0; index < val1.length; ++index) {
          let val_1 = val1[index];
          let val_2 = val2[index];

          handle_object_function(val_1,null,val_2,null);
        }
      } else {
        for (let key_1 of Object.keys(val1)) {

          let val_1 = val1[key_1]
          if (key_1 in val2 === false) {
            buff.push(false)
            return;
          }
          handle_object_function(val_1, key_1, val2[key_1], key_1);
        }
      }
  } 

  handle_object_function(obj1, null, obj2, null);

  if(buff.indexOf(false) >= 0)
    return false;
  return true;
};