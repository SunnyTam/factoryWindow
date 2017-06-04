/**
 * Created by Sunny on 3/6/2017.
 */

function onDdlSelected(selectedFabric, selectedClothing) {
    $(".overlay").fadeOut("slow");
    // console.log(selectedFabric);
    // console.log(selectedClothing);
    // console.log(selectedFabric != '' && selectedClothing != '');
    if(selectedFabric !== '' && selectedClothing !== '') {
        $('.pin').show();
    } else {
        $('.pin').hide();
    }
}

$(function () {
    $('.ui.dropdown').dropdown();

    var selectedFabric = '';
    var selectedClothing = '';

   $('.fabric-ddl select').change(function(){
       selectedFabric = $('.fabric-ddl select').val();
       onDdlSelected(selectedFabric, selectedClothing);
   });

    $('.clothing-ddl select').change(function(){
        selectedClothing = $('.clothing-ddl select').val();
        onDdlSelected(selectedFabric, selectedClothing);
   });
});