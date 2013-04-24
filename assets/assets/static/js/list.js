$(function(){

  // Hide all sort arrows
  $('.down_arrow').hide();
  $('.up_arrow').hide();

  $('.sort').find('a').click(function(){
    update_sorts($(this));
  });
});

function update_sorts(dis){
  var sort_order = dis.data('sort_order');
  var _this = dis;
  var sorts = {};
  var query = '?ajax=1';

  // Mask the element so that the user may not double-click and mess up the sort
  $(this).closest('.wrapper').mask('sorting..');


  // Update sorts
  if(typeof(sort_order) == 'undefined' || sort_order == 'asc'){
    _this.data('sort_order', 'desc');
    _this.parent().find('.down_arrow').show();
    _this.parent().find('.up_arrow').hide();
  } else {
    _this.data('sort_order', 'asc');
    _this.parent().find('.up_arrow').show();
    _this.parent().find('.down_arrow').hide();
  }


  // Set url sorts
  window.sorts.forEach(function(key, value){
    query += key + '=' + value + '&';
  });

  console.log(sorts);

  $.get(window.sort_url+query, function(data){
    $('.object-list').html(data);
    // Hide all sort arrows
    $('.down_arrow').hide();
    $('.up_arrow').hide();

    $('.sort').find('a').click(function(){
      update_sorts($(this));
    });
    $('.wrapper').unmask();
  }).fail(function(){
    alert("the system encountered an error");
    $('.wrapper').unmask();
  });
}

function update_arrows(){}