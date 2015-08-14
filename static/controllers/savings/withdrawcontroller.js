angular.module('gosaccoApp')
   .controller('WithdrawCtrl', ['$scope','Member', function($scope,Member){
       $scope.members = Member.query();
   	   var vm = this;
   	   vm.withdraw = {};
   	  // vm.withdrawFields = [
   	  // {
      //       key: 'member',
      //       type: 'select',
      //       templateOptions: {
      //           label: 'Member Name',
      //           options:[
      //           {name:"Buhiire Keneth", value:"Buhiire Keneth"},
      //           {name:"Semakula Kraiba", value:"Semakula Kraiba"},
      //           {name:"Lubega Mark", value:"Lubega Mark"},
      //           {name:"Ricardo Mandela", value:"Ricardo Mark"}],
      //           placeholder:"Select a member",
      //           required: true
      //       }
      //   },
      //   {
      //       key: 'amount',
      //       type: 'input',
      //       templateOptions: {
      //           type: 'text',
      //           label: 'Amount',
      //           required: true
      //       }
   	  // },
   	  // {
   	  // 	    key:'saving_type',
   	  // 	    type:'input',
   	  // 	    templateOptions:{
   	  // 	    	type:'date',
   	  // 	    	label:"Date",
   	  // 	    	required:true
   	  // 	    }
   	  // }];
   }]);
