var abc = angular.module('abc', []);
//scope connects html elements to things in scope
abc.controller('ctrl', function($scope){/*controller fn here needs controller name and a factory function-->*/
		var vm = this;
		vm.first ='a';
	
		vm.print = function(){
			vm.tbp = "qwerty"+vm.first;
		};
	});