var socket = io.connect('ws://' + document.domain + ':8090');
socket.on('connect', function() {
    console.log('socket connect success')
});
socket.on('close', function() {
    console.log("closed")
});

// 主承运商按商户查询
socket.on('agent_retailer', function(msg){
    $("#result").append(msg)
});
$("#agent_retailer").click(function(){
  $("#result").empty("");
  var retailer_id = $('#agent_retailer_id').val();
  socket.emit('agent_retailer', {
      retailer_id : retailer_id
  })
});
