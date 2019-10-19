// const monomials = [
//   ['0000', '0010', '0020', '2000', '2010'],
//   ['0010', '0020', '2000', '2010', '2020'],
//   ['0000', '0110', '0220', '3000', '3110'],
//   ['0110', '0220', '3000', '3110', '3220'],
//   ['0000', '0100', '0200', '1000', '1100'],
//   ['0100', '0200', '1000', '1100', '1200'],
//   ['0010', '0110', '0210', '1010', '1110'],
//   ['0110', '0210', '1010', '1110', '1210'],
//   ['0010', '0120', '2200', '3010', '3120'],
//   ['0020', '0120', '0220', '1020', '1120'],
//   ['0120', '0220', '1020', '1120', '1220'],
//   ['2000', '2100', '2200', '3000', '3100'],
//   ['2100', '2200', '3000', '3100', '3200'],
//   ['2010', '2110', '2210', '3010', '3110'],
//   ['2110', '2210', '3010', '3110', '3210'],
//   ['2010', '2100', '0220', '1010', '1100'],
//   ['2020', '2120', '2220', '3020', '3120'],
//   ['2120', '2220', '3020', '3120', '3220'],
//   ['2020', '2110', '2200', '1020', '1110'],
//   ['2110', '2200', '1020', '1110', '1200'],
//   ['0100', '0110', '0120', '2100', '2110'],
//   ['0110', '0120', '2100', '2110', '2120'],
//   ['0100', '0210', '1020', '3100', '3210'],
//   ['0200', '0210', '0220', '2200', '2210'],
//   ['0210', '0220', '2200', '2210', '2220'],
//   ['1000', '1010', '1020', '3000', '3010'],
//   ['1010', '1020', '3000', '3010', '3020'],
//   ['1100', '1110', '1120', '3100', '3110'],
//   ['1110', '1120', '3100', '3110', '3120'],
//   ['1200', '1210', '1220', '3200', '3210'],
//   ['1210', '1220', '3200', '3210', '3220'],
//   ['1210', '1120', '3000', '2210', '2120']
// ]

const monomials = [
  ['0000', '0010', '0020', '2000', '2010'],
  ['0010', '0020', '2000', '2010', '2020'],
  ['0000', '0110', '0220', '3000', '3110'],
  ['2010', '2100', '0220', '1010', '1100'],
  ['1210', '1120', '3000', '2210', '2120']
]

var empty = []


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//rotate4
//nothing to include => innermost function being called
var rotate4 = function(quadrant, array){

  let direction = 0
  let count = 0
  while (count < 4){

    array = JSON.parse(JSON.stringify(array));

    for (let i = 0; i < array.length; i++){
      for (let j = 0; j < 5; j++){

        if (array[i][j].charAt(0) == `${quadrant}`){
          array[i][j] = array[i][j].replace(/.$/,direction.toString())
        }
      }
    }
    empty.push(array)

    direction++
    count++
  }
}
// rotate4("1", monomials)



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//rotate3
//include rotate4
var rotate3 = function(quadrant, array){

  let direction = 0
  let count = 0
  while (count < 4){

    array = JSON.parse(JSON.stringify(monomials));

    for(let i = 0; i < array.length; i++){
      for(let j = 0; j < 5; j++){
        if (array[i][j].charAt(0) == `${quadrant}`){
          array[i][j] = array[i][j].replace(/.$/,direction.toString())
        }
      }
    }

    rotate4("3", array)
    empty.push(array)
    direction++
    count++
  }

  // console.log('output of empty array')
  // console.log(empty)
  // console.log(`empty length: ${empty.length}`)
}
// rotate3("1", monomials)



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//rotate2
//include rotate3
  var rotate2 = function(quadrant, array){

    let direction = 0
    let count = 0
    while (count < 4){

      array = JSON.parse(JSON.stringify(monomials));

      for(let i = 0; i < array.length; i++){
        for(let j = 0; j < 5; j++){
          if (array[i][j].charAt(0) == `${quadrant}`){
            array[i][j] = array[i][j].replace(/.$/,direction.toString())
          }
        }
      }

      rotate3("2", array)
      empty.push(array)
      direction++
      count++
    }

    // console.log('output of empty array')
    // console.log(empty)
    // console.log(`empty length: ${empty.length}`)
  }
  // rotate2("1", monomials)



/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//rotate1
  //include rotate2
  var rotate1 = function(quadrant, array){

    let direction = 0
    let count = 0
    while (count < 4){

      array = JSON.parse(JSON.stringify(monomials));

      for(let i = 0; i < array.length; i++){
        for(let j = 0; j < 5; j++){
          if (array[i][j].charAt(0) == `${quadrant}`){
            array[i][j] = array[i][j].replace(/.$/,direction.toString())
          }
        }
      }

      rotate2("1", array)
      empty.push(array)
      direction++
      count++
    }


  }
  rotate1("0", monomials)


  console.log("this is monomials array:")
  console.log(monomials)
  console.log('output of empty array')
  console.log(empty)
  console.log(`empty length: ${empty.length}`)


  //changes in 0000 to 0001, 0002, 0003 out of range of arrays being displayed in terminal.
  //random searching to check if changes are occuring.
  // for (let i = 100; i < 200; i++){
  //   console.log(`value at array 'empty' ${i}:`)
  //   console.log(empty[i])
  // }

  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
