
var TimeLimitedCache = function() {
    this.caches = [];
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
  let cache = this.caches.find(cache => cache.key === key);
  if (cache == null) {
    const obj = {};
    obj.key = key;
    obj.value = value;
    obj.expire = Date.now() + duration;

    this.caches.push(obj)
    return false;
  } else {
    cache.value = value;
    cache.expire = Date.now() + duration;
    return true;
  }

};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
  curDate = Date.now()
  this.caches = this.caches.filter(function(cache) {
      return cache.expire > curDate;
  });

  let cache = this.caches.find(cache => cache.key === key);
  if (cache == null)
      return -1;
  else
      return cache.value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
  curDate = Date.now()
  this.caches = this.caches.filter(function(cache) {
      return cache.expire > curDate;
  });
  return this.caches.length;
};

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */