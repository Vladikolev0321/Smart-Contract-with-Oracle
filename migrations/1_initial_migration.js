const BitcoinPriceOracle = artifacts.require("BitcoinPriceOracle");
const HelloWorld = artifacts.require("HelloWorld");

module.exports = function (deployer) {
  deployer.deploy(BitcoinPriceOracle);
};
