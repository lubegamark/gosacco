/**
 * Created by leona on 5/18/15.
 */
'use strict';
angular.module('gosaccoApp',['ngResource', 'ngRoute'])
.config(['$routeProvider','$locationProvider',function($routeProvider, $locationProvider){
      // $locationProvider.html5Mode(true);
      $routeProvider
      .when('/home',{
      	templateUrl:'views/home.html',
      	controller:'BaseCtrl'
      })
      .when('/members',{
      	templateUrl:'views/members.html',
      	controller:'MemberCtrl'
      })
      .when('/savings',{
      	templateUrl:'views/savings.html',
      	controller:'SavingCtrl'
      })
      .when('/loans',{
      	templateUrl:'views/loans.html',
      	controller:'LoanCtrl'
      })
      .when('/shares',{
      	templateUrl:'views/shares.html',
      	controller:'ShareCtrl'
      })
      .when('/others',{
      	templateUrl:'views/others.html',
      	controller:'OtherCtrl'
      })
      .when('/accounting',{
      	templateUrl:'views/accounting.html',
      	controller:'AccountingCtrl'
      })
      .when('/reports',{
      	templateUrl:'views/reports.html',
      	controller:'ReportCtrl'
      })
      .when('/notifications',{
      	templateUrl:'views/notifications.html',
      	controller:'NotificationCtrl'
      })
      .when('/settings',{
      	templateUrl:'views/settings.html',
      	controller:'SettingCtrl'
      }).otherwise({redirectTo:'/'});
    }]);