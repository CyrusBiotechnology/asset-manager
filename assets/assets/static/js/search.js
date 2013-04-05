
var search_element = '#search';
var results_element = '#search-results';
var search_url = 'se?q=';

SR_template = 'search-result-template';

function query() {
  var q = $(search_element).val();
  $(results_element).html('');

  // Is the query blank?
  if(q === ''){ return; }

  $.get(search_url+q, function(data){
    $.each(data, function(){
      window.search_res = this;
      $(results_element).html($.Mustache.render(SR_template, this));
    });
  });
}

$(function(){
  $(search_element).watermark('search...');
  $(search_element).keyupQueue(function () {
    query();
  });
});