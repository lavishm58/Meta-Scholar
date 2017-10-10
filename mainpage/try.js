var casper = require('casper').create({
	pageSettings:{
		userAgent:"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36"
	}
	,clientScripts: ['/home/gamechanger/Documents/src/jquery-1.6.1.js']

});

    
    
var query=casper.cli.get('query');
var page = casper.cli.get('page');

var arofquery = query.split(' ');
var iarofquery = arofquery;
arofquery = arofquery.join(' ');
iarofquery = iarofquery.join(' ');

var intpage=parseInt(page);
if (intpage>2){
var num=8*(parseInt(page)-2);
} else {
	var num = 0;
}
var fr=num.toString();

var url='https://academic.microsoft.com/#/search?iq='+'@'+arofquery+'@'+'&q='+iarofquery+"&filters=&from="+fr+"&sort=0"
// console.log(url);
var currentPage=1;
var articles=[];

var terminate=function() {
	this.echo('Exiting..').exit;
};

var processPage = function() {
	var articles=this.evaluate(getArticles);
	require('utils').dump(articles);


};

var processPage2 = function() {
	var articles=this.evaluate(getArticles2);
};

function getArticles2(){	
	var rows=document.querySelectorAll('article.paper-tile2');
};


function getArticles(){	
	var rows=document.querySelectorAll('article.paper-tile2');
	var page=document.querySelector('ul#searchControl');
	// this.clickLabel('-0.875','a');
	var articles='';
	for (var i=0,row;row=rows[i];i++){
		var a=row.querySelector('a')
		var d=row.querySelector('p')
		articles=articles+a.innerText+'`';
		articles=articles+'https://academic.microsoft.com/'+a.getAttribute('href')+'`';
		articles=articles+d.innerText+'`';
	}
	return articles;
};

casper.start(url,function(){
	this.waitForSelector('ul[id="searchControl"]');
});

// casper.then(function() {
//     console.log('clicked ok, new location is ' + this.getCurrentUrl());
    
// });
casper.waitForSelector('ul.pagination',processPage2,terminate);
casper.then(function(){
	if (intpage>1){
	this.clickLabel(page,'a');
	this.waitForSelector('ul[id="searchControl"]');
}
});
casper.waitForSelector('ul.pagination',processPage2,terminate);
casper.then(function(){
	if (intpage>1)	{
	this.clickLabel(page,'a');
	this.waitForSelector('ul[id="searchControl"]');
}
});

casper.then(function(){
	if (intpage>2)	{
	this.clickLabel(page,'a');
	this.waitForSelector('ul[id="searchControl"]');
}
});

// casper.then(function() {
//     console.log('clicked ok, new location is ' + this.getCurrentUrl());
// });
casper.waitForSelector('ul.pagination',processPage,terminate);

casper.run();