---
title: "Các kiểu for JavaScript"
date: 2025-08-01
---

# Các kiểu for data trong JavaScript

## List

#### 1. for truyền thống (theo chỉ số)

```js
const list = ['a', 'b', 'c'];

for (let i = 0; i < list.length; i++) {
  console.log(list[i]);
}
```

✅ Ưu điểm: kiểm soát được chỉ số, có thể break, continue.

#### 2. for...of (lặp qua giá trị phần tử)

```js
for (const item of list) {
  console.log(item);
}
```

✅ Rõ ràng, dễ đọc. Không truy cập được chỉ số trực tiếp.

#### 3. for...in (lặp qua chỉ số/khóa – KHÔNG khuyến nghị dùng cho mảng)

```js
for (const index in list) {
  console.log(index, list[index]);
}
```

⚠️ Chủ yếu dùng cho object. Với mảng có thể gây lỗi nếu có thuộc tính không phải chỉ số.

#### 4. forEach() (hàm callback)

```js
list.forEach((item, index) => {
  console.log(index, item);
});
```

✅ Rất phổ biến. Không thể dùng break hay continue.

#### 5. map() (tạo mảng mới từ mảng cũ)

```js
const newList = list.map((item, index) => item.toUpperCase());
```

✅ Dùng khi cần biến đổi mảng.

#### 6. while và do...while

```js
let i = 0;
while (i < list.length) {
  console.log(list[i]);
  i++;
}
```

## Object

#### 1. for...in – Lặp qua key (tên thuộc tính)

```js
const obj = { name: 'Tuấn', age: 25 };

for (const key in obj) {
  console.log(key, obj[key]);
}
```
👉 Duyệt qua tất cả các key trong object (bao gồm cả kế thừa, nên nên dùng với hasOwnProperty() nếu cần lọc).

#### 2. Object.keys() + forEach – Lặp qua key

```js
Object.keys(obj).forEach(key => {
  console.log(key, obj[key]);
});
```

✅ An toàn hơn for...in vì không lấy thuộc tính kế thừa.

#### 3. Object.values() – Lặp qua giá trị

```js
Object.values(obj).forEach(value => {
  console.log(value);
});
```

#### 4. Object.entries() – Lặp qua [key, value]

```js
for (const [key, value] of Object.entries(obj)) {
  console.log(key, value);
}
```

✅ Cách rất gọn và phổ biến khi cần cả key và value.

#### 5. Duyệt bằng forEach() (sau khi chuyển sang mảng)

```js
const obj = { name: 'Tuấn', age: 25 };

Object.entries(obj).forEach(([key, value]) => {
  console.log(`${key}: ${value}`);
});
```

❌ Không nên dùng: for...of trực tiếp với object

```js
const obj = { name: 'Tuấn', age: 25 };

// ❌ Sai: TypeError
for (const item of obj) {
  console.log(item);
}
```

⚠️ for...of chỉ dùng được với iterable (array, string, Set, Map…), còn object thì không. Nếu muốn, bạn phải dùng Object.entries() để biến object thành mảng trước.

## new Set()

#### Ví dụ Set cơ bản:

```js
const mySet = new Set(['apple', 'banana', 'cherry']);
```

#### 1. for...of – Duyệt qua giá trị

```js
for (const value of mySet) {
  console.log(value);
}
```

✅ Đây là cách phổ biến nhất. Set là iterable nên for...of hoạt động trực tiếp.

#### 2. forEach() – Hàm callback

```js
mySet.forEach((value) => {
  console.log(value);
});
```

✅ Giống với mảng Array.forEach, nhưng tham số đầu tiên là giá trị, và cả tham số thứ nhất và thứ hai đều là value (vì Set không có key).


```js
mySet.forEach((value, againValue) => {
  console.log(value, againValue); // giống nhau
});
```

#### 3. Duyệt qua mySet.values() hoặc mySet.keys()

```js
for (const value of mySet.values()) {
  console.log(value);
}
```

```js
for (const key of mySet.keys()) {
  console.log(key); // giống values()
}
```

👉 Trong Set, .keys() và .values() đều trả về giá trị giống nhau, vì Set không có key.

#### 4. Duyệt qua mySet.entries() (cặp [value, value])

```js
for (const [key, value] of mySet.entries()) {
  console.log(key, value); // giống nhau
}
```

⚠️ Dùng để tương thích với các hàm map, nhưng cả key và value đều là giá trị của phần tử.

#### 5. Dùng spread (...) và for

```js
const arr = [...mySet];
for (let i = 0; i < arr.length; i++) {
  console.log(arr[i]);
}
```

👉 Dùng nếu bạn muốn truy cập theo chỉ số, Set không hỗ trợ điều này trực tiếp.

## new Map()

Ví dụ Map cơ bản:

```js
const myMap = new Map();
myMap.set('name', 'Tuấn');
myMap.set('age', 25);
myMap.set({ id: 1 }, 'UserObject');
```

#### 1. for...of – Duyệt qua Map trực tiếp (trả về [key, value])

```js
for (const [key, value] of myMap) {
  console.log(key, value);
}
```

✅ Đây là cách phổ biến nhất và rất gọn gàng để duyệt tất cả key-value.

#### 2. .forEach() – Gọi callback với từng cặp

```js
myMap.forEach((value, key) => {
  console.log(key, value);
});
```

⚠️ Trong Map, thứ tự tham số trong forEach là (value, key) – ngược với object thường (hay so với mảng .forEach(index, value)).

#### 3. map.keys() – Duyệt qua key

```js
for (const key of myMap.keys()) {
  console.log(key);
}
```

#### 4. map.values() – Duyệt qua value

```js
for (const value of myMap.values()) {
  console.log(value);
}
```

#### 5. map.entries() – Duyệt qua [key, value]

```js
for (const [key, value] of myMap.entries()) {
  console.log(key, value);
}
```

✅ Giống như for...of myMap – vì Map mặc định iterable bằng .entries().

#### 6. Chuyển sang Array nếu cần

```js
const entriesArray = Array.from(myMap); // [[key, value], ...]
entriesArray.forEach(([key, value]) => {
  console.log(key, value);
});
```

👉 Hữu ích nếu bạn muốn sort, filter, v.v.