var strat = {};

strat.init = function(){
	console.log('init');
}




strat.check = function(candle){
	console.log(candle.start.format('Y'));
	console.log(candle.start.format('M'));
	console.log(candle.start.format('D'));


}

module.exports = strat;