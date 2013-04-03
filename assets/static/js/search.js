
var search_element = '#search';
var search_url = 'se?q=';

function query(element) {
  var q = $(element).val();
  $.get(search_url+q, function(data){
    console.log(data);
  });
}

$(function(){
  $(search_element).watermark('search...');
  $(search_element).keyupQueue(function () {
    query(search_element);
  });
});