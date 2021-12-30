function myPow(x: number, n: number): number {
  // takes much time
  //     if( n ===0) 
  //         return 1
  //     if(n === -1) {
  //         return 1/x
  //     }
  //     if( n === 1 ) {
  //         return x
  //     }

  //     if(n > 1)
  //         return myPow(x,n-1) * x
  //     return myPow(x,n+1) * (1/x)
// takes less time becz its memoized
  if (n < 0) {
    const y = dohalfWork(x, new Map(), n * -1);
    return (1 / y)
  }

  return dohalfWork(x, new Map(), n)
};

function newPow(x: number, n: number): number {
  if (n === 0)
    return 1

  if (n === 1) {
    return x
  }

  if (n === 2)
    return x * x

};

function dohalfWork(x: number, dic: Map<number, number>, pivot: number): number {

  const leftHalfOfThePivot: number = Math.ceil(pivot / 2);
  const rightHalfOfThePivot: number = pivot - leftHalfOfThePivot;
  let leftSideOfThePower: number;
  let rightSideOfThePower: number;

  //leftSide
  if (dic.get(leftHalfOfThePivot)) {
    leftSideOfThePower = dic.get(leftHalfOfThePivot)
  } else if (leftHalfOfThePivot < 2) {
    leftSideOfThePower = newPow(x, leftHalfOfThePivot)
    dic.set(leftHalfOfThePivot, leftSideOfThePower);
  } else {
    leftSideOfThePower = dohalfWork(x, dic, leftHalfOfThePivot);
    dic.set(leftHalfOfThePivot, leftSideOfThePower);
  }

  if (dic.get(rightHalfOfThePivot)) {
    rightSideOfThePower = dic.get(rightHalfOfThePivot)
  } else if (rightHalfOfThePivot < 2) {
    rightSideOfThePower = newPow(x, rightHalfOfThePivot)
    dic.set(rightHalfOfThePivot, rightSideOfThePower);
  } else {
    rightSideOfThePower = dohalfWork(x, dic, rightHalfOfThePivot);
    dic.set(rightHalfOfThePivot, rightSideOfThePower);
  }

  return rightSideOfThePower * leftSideOfThePower;
}