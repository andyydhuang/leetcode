/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
  //let temp_str = ''
  let buff = []

  var handle_object_function = function(value, key) {
    //console.log('=============')
    //console.log(`${key}: ${value}`);

      if (key !== null)
        //temp_str = temp_str.concat(`"${key}":`);
        buff.push(`"${key}":`)
      if (value === null) {
        //temp_str = temp_str.concat(`null`);
        buff.push('null')
      } else if (typeof value !== 'object') {
        if (typeof value === 'string')
          //temp_str = temp_str.concat(`"${value}"`);
          buff.push(`"${value}"`)
        else
          //temp_str = temp_str.concat(`${value}`);
          buff.push(`${value}`)
      } else if (Object.keys(value).length === 0) {
        if (value.hasOwnProperty('length') === true)
          //temp_str = temp_str.concat(`[]`);
          buff.push(`[]`)
        else
          //temp_str = temp_str.concat(`{}`);
          buff.push(`{}`)
      } else if (Array.isArray(value) === true) {
        //temp_str = temp_str.concat(`[`);
        buff.push(`[`);
        for (let index = 0; index < value.length; ++index) {
          let val = value[index];
          let val_type = typeof value[index];
          if (val === null)
            //temp_str = temp_str.concat(`null`);
            buff.push('null');
          else if (val_type !== 'object') {
            if (val_type === 'string')
              //temp_str = temp_str.concat(`"${val}"`);
              buff.push(`"${val}"`);
            else
              //temp_str = temp_str.concat(`${val}`);
              buff.push(`${val}`);
          }
          else
            handle_object_function(val,null);
          //temp_str = temp_str.concat(`,`);
          buff.push(',');
        }
        //temp_str = temp_str.slice(0, -1); 
        buff.pop();
        //temp_str = temp_str.concat(`]`);
        buff.push(']');
      } else {
        //temp_str = temp_str.concat(`{`);
        buff.push('{');
        for (const [key, val] of Object.entries(value)) {
          handle_object_function(val, key);
          //temp_str = temp_str.concat(`,`);
          buff.push(',');
        }
        //temp_str = temp_str.slice(0, -1);
        buff.pop();
        //temp_str = temp_str.concat(`}`);
        buff.push('}');
      } 
  } 

  handle_object_function(object, null);
  //return temp_str;
  return buff.join('')
};