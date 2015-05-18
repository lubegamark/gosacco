/**
 * Created by leona on 5/18/15.
 */
'use strict';
angular.module('gosaccoApp',['ngResource', 'ngRoute'])
.config(['$routeProvider','$locationProvider',function($routeProvider, $locationProvider){
      $locationProvider.html5Mode(true);
    }]);