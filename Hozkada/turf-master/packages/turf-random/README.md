# @turf/random

<!-- Generated by documentation.js. Update this documentation by updating the source code. -->

## randomPosition

Returns a random position within a [box][1].

### Parameters

*   `bbox` **[Array][2]<[number][3]>** a bounding box inside of which positions are placed. (optional, default `[-180,-90,180,90]`)

### Examples

```javascript
var position = turf.randomPosition([-180, -90, 180, 90])
// => position
```

*   Throws **[Error][4]** if bbox is invalid

Returns **[Array][2]<[number][3]>** Position \[longitude, latitude]

## randomPoint

Returns a random [point][5].

### Parameters

*   `count` **[number][3]** how many geometries will be generated (optional, default `1`)
*   `options` **[Object][6]** Optional parameters (optional, default `{}`)

    *   `options.bbox` **[Array][2]<[number][3]>** a bounding box inside of which geometries are placed. (optional, default `[-180,-90,180,90]`)

### Examples

```javascript
var points = turf.randomPoint(25, {bbox: [-180, -90, 180, 90]})
// => points
```

*   Throws **[Error][4]** if bbox is invalid

Returns **[FeatureCollection][7]<[Point][8]>** GeoJSON FeatureCollection of points

## randomPolygon

Returns a random [polygon][9].

### Parameters

*   `count` **[number][3]** how many geometries will be generated (optional, default `1`)
*   `options` **[Object][6]** Optional parameters (optional, default `{}`)

    *   `options.bbox` **[Array][2]<[number][3]>** a bounding box inside of which geometries are placed. (optional, default `[-180,-90,180,90]`)
    *   `options.num_vertices` **[number][3]** is how many coordinates each LineString will contain. (optional, default `10`)
    *   `options.max_radial_length` **[number][3]** is the maximum number of decimal degrees latitude or longitude that a
        vertex can reach out of the center of the Polygon. (optional, default `10`)

### Examples

```javascript
var polygons = turf.randomPolygon(25, {bbox: [-180, -90, 180, 90]})
// => polygons
```

*   Throws **[Error][4]** if bbox is invalid

Returns **[FeatureCollection][7]<[Polygon][10]>** GeoJSON FeatureCollection of polygons

## randomLineString

Returns a random [linestring][11].

### Parameters

*   `count` **[number][3]** how many geometries will be generated (optional, default `1`)
*   `options` **[Object][6]** Optional parameters (optional, default `{}`)

    *   `options.bbox` **[Array][2]<[number][3]>** a bounding box inside of which geometries are placed. (optional, default `[-180,-90,180,90]`)
    *   `options.num_vertices` **[number][3]** is how many coordinates each LineString will contain. (optional, default `10`)
    *   `options.max_length` **[number][3]** is the maximum number of decimal degrees that a
        vertex can be from its predecessor (optional, default `0.0001`)
    *   `options.max_rotation` **[number][3]** is the maximum number of radians that a
        line segment can turn from the previous segment. (optional, default `Math.PI/8`)

### Examples

```javascript
var lineStrings = turf.randomLineString(25, {bbox: [-180, -90, 180, 90]})
// => lineStrings
```

*   Throws **[Error][4]** if bbox is invalid

Returns **[FeatureCollection][7]<[LineString][12]>** GeoJSON FeatureCollection of linestrings

[1]: bounding

[2]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Array

[3]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Number

[4]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error

[5]: point

[6]: https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Object

[7]: https://tools.ietf.org/html/rfc7946#section-3.3

[8]: https://tools.ietf.org/html/rfc7946#section-3.1.2

[9]: polygon

[10]: https://tools.ietf.org/html/rfc7946#section-3.1.6

[11]: linestring

[12]: https://tools.ietf.org/html/rfc7946#section-3.1.4

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
$ npm install @turf/random
```

Or install the Turf module that includes it as a function:

```sh
$ npm install @turf/turf
```