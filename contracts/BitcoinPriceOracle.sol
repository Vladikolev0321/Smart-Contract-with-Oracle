pragma solidity ^0.8.5;


contract BitcoinPriceOracle {
    string public currPriceUSD;

    function updateCurrPrice(string memory _currPriceUSD) public {
        currPriceUSD = _currPriceUSD;
    }
}