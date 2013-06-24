
var search_element = '.filter';
var results_element = '#search-results';
var search_url = 'se?';
var filter_count = 1;

SR_template = '';

function query() {
  window.q = '';
  // Loop through each filter
  $(search_element).each(function(){
    // If the filter is blank, skip it.
    if($(this).val() !== '') {
      // Get the field name
      param_str = $(this).siblings('.field-select').val();
      // Get the field value
      param_str += '=' + $(this).val() + '&';
      // Append it to the parameter string
      window.q += param_str;
    }
  });

  $(results_element).html('');

  $.get(search_url+window.q, function(data){
    $.each(data, function(){
      search_res = this.fields;
      window.search_res = this;
      console.log(search_res);
      $(results_element).append(Mustache.render(SR_template, this));
    });
  });
}

$(function(){
  
  $('.search-filter').last().after($('.search-filter-template').last().clone(withDataAndEvents=true));
  $('.search-filter-template').last().removeClass('search-filter-template');

  $('.add-filter').click(function(){
    $('.search-filter').last().after($('.search-filter-template').last().clone(withDataAndEvents=true));
    $('.search-filter-template').last().removeClass('search-filter-template');
	$(filter_count ++);
  });

  $('.remove-filter').click(function(){
    $('.search-filter').last().remove();
	$(filter_count --);
  });
  
  $(search_element).focus();
  SR_template = $('#search-result-template').html();
  $(search_element).watermark('filter...');
  $(search_element).keyupQueue(function () {
    query();
  });
  $('.field-select').change(function(){
    query();
  });
});