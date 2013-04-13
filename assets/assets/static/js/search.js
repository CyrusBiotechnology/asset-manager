
var search_element = '#search';
var results_element = '#search-results';
var search_url = 'se?q=';

SR_template = '';

function query() {
  var q = $(search_element).val();
  $(results_element).html('');

  // Is the query blank?
  if(q === ''){ return; }

  $.get(search_url+q, function(data){
    $.each(data, function(){
      search_res = this.fields;
      window.search_res = this;
      console.log(this);
      console.log(SR_template);
      console.log(Mustache.render(SR_template, this));
      $(results_element).html(Mustache.render(SR_template, this));
    });
  });
}

$(function(){
  $(search_element).focus();
  SR_template = $('#search-result-template').html();
  $(search_element).watermark('search...');
  $(search_element).keyupQueue(function () {
    query();
  });
});