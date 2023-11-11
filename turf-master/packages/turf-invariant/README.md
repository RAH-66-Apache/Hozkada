# @turf/invariant

<!-- Generated by documentation.js. Update this documentation by updating the source code. -->

## getCoord

Unwrap a coordinate from a Point Feature, Geometry or a single coordinate.

### Parameters

*   `coord` **([Array][1]<[number][2]> | [Geometry][3]<[Point][4]> | [Feature][5]<[Point][4]>)** GeoJSON Point or an Array of numbers

### Examples

```javascript
var pt = turf.point([10, 10]);

var coord = turf.getCoord(pt);
//= [10, 10]
```

Returns **[Array][1]<[number][2]>** coordinates

## getCoords

Unwrap coordinates from a Feature, Geometry Object or an Array

### Parameters

*   `coords` **([Array][1]\<any> | [Geometry][3] | [Feature][5])** Feature, Geometry Object or an Array

### Examples

```javascript
var poly = turf.polygon([[[119.32, -8.7], [119.55, -8.69], [119.51, -8.54], [119.32, -8.7]]]);

var coords = turf.getCoords(poly);
//= [[[119.32, -8.7], [119.55, -8.69], [119.51, -8.54], [119.32, -8.7]]]
```

Returns **[Array][1]\<any>** coordinates

## containsNumber

Checks if coordinates contains a number

### Parameters

*   `coordinates` **[Array][1]\<any>** GeoJSON Coordinates

Returns **[boolean][6]** true if Array contains a number

## geojsonType

Enforce expectations about types of GeoJSON objects for Turf.

### Parameters

*   `value` **[GeoJSON][7]** any GeoJSON object
*   `type` **[string][8]** expected GeoJSON type
*   `name` **[string][8]** name of calling function

<!---->

*   Throws **[Error][9]** if value is not the expected type.

## featureOf

Enforce expectations about types of [Feature][10] inputs for Turf.
Internally this uses [geojsonType][11] to judge geometry types.

### Parameters

*   `feature` **[Feature][5]** a feature with an expected geometry type
*   `type` **[string][8]** expected GeoJSON type
*   `name` **[string][8]** name of calling function

<!---->

*   Throws **[Error][9]** error if value is not the expected type.

## collectionOf

Enforce expectations about types of [FeatureCollection][12] inputs for Turf.
Internally this uses [geojsonType][11] to judge geometry types.

### Parameters

*   `featureCollection` **[FeatureCollection][13]** a FeatureCollection for which features will be judged
*   `type` **[string][8]** expected GeoJSON type
*   `name` **[string][8]** name of calling function

<!---->

*   Throws **[Error][9]** if value is not the expected type.

## getGeom

Get Geometry from Feature or Geometry Object

### Parameters

*   `geojson` **([Feature][5] | [Geometry][3])** GeoJSON Feature or Geometry Object

### Examples

```javascript
var point = {
  "type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Point",
    "coordinates": [110, 40]
  }
}
var geom = turf.getGeom(point)
//={"type": "Point", "coordinates": [110, 40]}
```

*   Throws **[Error][9]** if geojson is not a Feature or Geometry Object

Returns **([Geometry][3] | null)** GeoJSON Geometry Object

## getType

Get GeoJSON object's type, Geometry type is prioritize.

### Parameters

*   `geojson` **[GeoJSON][7]** GeoJSON object
*   `_name` **[string][8]?** 
*   `name` **[string][8]** name of the variable to display in error message (unused) (optional, default `"geojson"`)

### Examples

```javascript
var point = {
  "type": "Feature",
  "properties": {},
  "geometry": {
    "type": "Point",
    "coordinates": [110, 40]
  }
}
var geom = turf.getType(point)
//="Point"
```

Returns **[string][8]** GeoJSON type

[1]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array

[2]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number

[3]: https://tools.ietf.org/html/rfc7946#section-3.1

[4]: https://tools.ietf.org/html/rfc7946#section-3.1.2

[5]: https://tools.ietf.org/html/rfc7946#section-3.2

[6]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Boolean

[7]: https://tools.ietf.org/html/rfc7946#section-3

[8]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/String

[9]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error

[10]: https://tools.ietf.org/html/rfc7946#section-3.2

[11]: #geojsontype

[12]: https://tools.ietf.org/html/rfc7946#section-3.3

[13]: https://tools.ietf.org/html/rfc7946#section-3.3

<!-- This file is automatically generated. Please don't edit it directly:
if you find an error, edit the source file (likely index.js), and re-run
./scripts/generate-readmes in the turf project. -->

---

This module is part of the [Turfjs project](http://turfjs.org/), an open source
module collection dedicated to geographic algorithms. It is maintained in the
[Turfjs/turf](https://github.com/Turfjs/turf) repository, where you can create
PRs and issues.

### Installation

Install this module individually:

```sh
$ npm install @turf/invariant
```

Or install the Turf module that includes it as a function:

```sh
$ npm install @turf/turf
```