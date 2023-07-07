class EventEmitter {
  
  constructor() {
    this.sub_list = [];
  }

  subscribe(event, cb) {
    let obj = {};
    obj[event] = cb;
    this.sub_list.push(obj);
    //console.log(this.sub_list);

    return {
        unsubscribe: () => {
            //console.log(arguments);
            let to_remove = this.sub_list.find(sub => sub[arguments[0]] != null);
            this.sub_list = this.sub_list.filter(sub => sub !== to_remove);
        }
    };
  }

  emit(event, args = []) {
    let res = []
    for (let index = 0; index < this.sub_list.length; ++index) {
      let sub_unit = this.sub_list[index];
      //console.log(sub_unit[event])
      if (sub_unit[event] != null)
        res.push(sub_unit[event](...args))
    }
    return res
  }

}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */