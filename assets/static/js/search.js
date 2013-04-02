
var search_element = '#search';

function query(element) {
  $.get('');
}

$(function(){
  $(search_element).watermark('search...');
  $(search_element).keyupQueue(function () {
    query();
  });
});