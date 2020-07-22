//Maya ASCII 2019 scene
//Name: biped.ma
//Last modified: Wed, Jul 22, 2020 12:16:59 AM
//Codeset: UTF-8
requires maya "2019";
requires "stereoCamera" "10.0";
requires -nodeType "rmanGlobals" -nodeType "PxrPathTracer" "RenderMan_for_Maya.py" "23.1 @ 2036321";
requires "mtoa" "3.2.2";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2019";
fileInfo "version" "2019";
fileInfo "cutIdentifier" "201907021615-48e59968a3";
fileInfo "osv" "Mac OS X 10.14.6";
fileInfo "license" "student";
createNode transform -s -n "persp";
	rename -uid "9D43B38F-4B44-282A-3F06-EA91731C209E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 123.33728315028189 176.18088465512787 134.56673195212267 ;
	setAttr ".r" -type "double3" -38.738352729600003 30.600000000000215 -1.8475655781177224e-15 ;
	setAttr ".rpt" -type "double3" 1.2365394873407681e-14 5.4699246954646749e-15 -5.3321355746509597e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "B10920D0-DF46-5D55-C366-0686CDBC8413";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999986;
	setAttr ".coi" 313.29978913872009;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 7.7717790603637651 3.1372404098510747 6.3873970038082843 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "89DD53E8-E14B-9800-EE07-9F8AA615EC39";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 10.373867069700303 1000.1308318970156 11.702515600491969 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "2B1B54F6-454C-6B71-2C3C-14AE7A0DE14E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 994.85635107731321;
	setAttr ".ow" 71.344888227699386;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 7.7717790603637695 5.2744808197021484 -0.97217115466363424 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "DD8A03B5-ED42-262E-F77F-B692765E5FD3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 108.47364173317335 1004.7238661549881 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "20A2223A-BC48-94F5-62D3-DEBC529F8766";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 996.47143623527154;
	setAttr ".ow" 64.257457825322533;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 1.7763568394002505e-15 108.47364173317335 8.2524299197165369 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "28BD6E2F-6147-DC0A-6B02-A8B73112B73F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1010.2875625415212 78.62000975785584 -3.0812787119076388 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D4CBF13A-2842-11DA-AA90-94AE58C6BE27";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 962.46098686159587;
	setAttr ".ow" 23.400984214638139;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 47.826575679925128 83.244489971701 -0.26758894324302673 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "fitSkeleton_crv";
	rename -uid "9E89ECDF-1048-2A8B-FD7A-0BB0A41C3801";
	setAttr ".ovdt" 2;
	setAttr ".rp" -type "double3" 0 -6.1629758220391547e-33 -0.027503000000000055 ;
	setAttr ".sp" -type "double3" 0 -6.1629758220391547e-33 -0.027503000000000055 ;
createNode nurbsCurve -n "fitSkeleton_crvShape" -p "fitSkeleton_crv";
	rename -uid "D3C03473-ED47-8392-A147-978C9C77E36E";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "fitSkeleton_crvShape1" -p "fitSkeleton_crv";
	rename -uid "110F043A-2443-B8E6-E4F7-2BBBB97A9494";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		31.194329177888111 1.5608462488677652e-31 3.7496717661336443
		31.194329177888111 1.5608462488677652e-31 -3.8046777661336413
		40.637239767043866 1.5608462488677652e-31 -3.8046777661336413
		40.637239767043866 1.5608462488677652e-31 -7.581826206088925
		50.080150356199617 1.5608462488677652e-31 -0.027500367382162771
		40.637239767043866 1.5608462488677652e-31 7.526820206088928
		40.637239767043866 1.5608462488677652e-31 3.7496717661336443
		31.194329177888111 1.5608462488677652e-31 3.7496717661336443
		;
createNode nurbsCurve -n "fitSkeleton_crvShape2" -p "fitSkeleton_crv";
	rename -uid "F53618ED-6D4A-EF15-192A-FCA54AD3E32B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-3.7771747661336423 1.5608462488677652e-31 30.563201752426252
		-3.7771747661336423 1.5608462488677652e-31 40.006112341581989
		-7.5543232060889274 1.5608462488677652e-31 40.006112341581989
		0 1.5608462488677652e-31 49.449022930737755
		7.5543232060889274 1.5608462488677652e-31 40.006112341581989
		3.7771747661336423 1.5608462488677652e-31 40.006112341581989
		3.7771747661336423 1.5608462488677652e-31 30.563201752426252
		-3.7771747661336423 1.5608462488677652e-31 30.563201752426252
		;
createNode transform -n "ct_root_loc" -p "fitSkeleton_crv";
	rename -uid "28E7D0B2-BB42-A2FD-A422-1E971EA28043";
createNode locator -n "ct_root_locShape" -p "ct_root_loc";
	rename -uid "45EA7350-DA46-A69B-AA6F-268FE2A872C6";
	setAttr -k off ".v";
createNode transform -n "ct_hip_loc" -p "ct_root_loc";
	rename -uid "BC48583A-624D-CFC1-A9DF-059CE8899D4E";
	setAttr ".t" -type "double3" 0 47.962421417236328 -2.1840825080871582 ;
createNode locator -n "ct_hip_locShape" -p "ct_hip_loc";
	rename -uid "7BF47D9A-4D45-4911-1626-7C89246FAEE7";
	setAttr -k off ".v";
createNode transform -n "lt_leg_01_loc" -p "ct_hip_loc";
	rename -uid "43EAC36B-D246-559E-3E22-9CB3F76CC2F6";
	setAttr ".t" -type "double3" 7.7717790603637695 -1.9911003112792969 -0.082278251647949219 ;
createNode locator -n "lt_leg_01_locShape" -p "lt_leg_01_loc";
	rename -uid "511283DC-8344-C98F-FBE6-8C8E40164FE9";
	setAttr -k off ".v";
createNode transform -n "lt_leg_02_loc" -p "lt_leg_01_loc";
	rename -uid "E7F2D4F6-F440-427C-B908-CB9BA29EEBC0";
	setAttr ".t" -type "double3" 0 -22.046630859375 3.9313309192657471 ;
createNode locator -n "lt_leg_02_locShape" -p "lt_leg_02_loc";
	rename -uid "5318D20E-1240-FF56-258D-56A710DA3E56";
	setAttr -k off ".v";
createNode transform -n "lt_leg_03_loc" -p "lt_leg_02_loc";
	rename -uid "BA3DF3F0-1F48-61A7-FE49-178FEDE2332B";
	setAttr ".t" -type "double3" 0 -18.650209426879883 -2.9584735631942749 ;
createNode locator -n "lt_leg_03_locShape" -p "lt_leg_03_loc";
	rename -uid "08510198-F849-4FF5-CF6E-97A95290D312";
	setAttr -k off ".v";
createNode transform -n "lt_leg_04_loc" -p "lt_leg_03_loc";
	rename -uid "69297C6B-F64D-C6CD-BD16-75BF0FDD8602";
	setAttr ".t" -type "double3" 0 -5.2744792770369031 11.008226037025452 ;
createNode locator -n "lt_leg_04_locShape" -p "lt_leg_04_loc";
	rename -uid "B99743AA-0145-80E3-ABE4-E6AA4F98783C";
	setAttr -k off ".v";
createNode transform -n "lt_leg_05_loc" -p "lt_leg_04_loc";
	rename -uid "DD35D88D-594C-6610-C6EE-1FAD34BEC5F4";
	setAttr ".t" -type "double3" 0 -2.1766588247373875e-06 6.8961896896362305 ;
createNode locator -n "lt_leg_05_locShape" -p "lt_leg_05_loc";
	rename -uid "5E0BA8B2-274B-13EA-80E7-E693C19FFC94";
	setAttr -k off ".v";
createNode transform -n "lt_toeA_01_loc" -p "lt_leg_04_loc";
	rename -uid "84723742-D642-EBEF-F71F-FD8EF1E394BD";
	setAttr ".t" -type "double3" -2.9625077247619629 -2.3190958700070041e-06 1.8733205795288086 ;
createNode locator -n "lt_toeA_01_locShape" -p "lt_toeA_01_loc";
	rename -uid "82772BC3-5546-F9B1-0259-21AD4009BAB1";
	setAttr -k off ".v";
createNode transform -n "lt_toeA_02_loc" -p "lt_toeA_01_loc";
	rename -uid "A3F16DA6-4841-6437-0BF4-DD90C884CF12";
	setAttr ".t" -type "double3" 0 0 2 ;
createNode locator -n "lt_toeA_02_locShape" -p "lt_toeA_02_loc";
	rename -uid "2FD4265B-6F43-5C1E-B4C5-16BF155B1CC4";
	setAttr -k off ".v";
createNode transform -n "lt_toeA_03_loc" -p "lt_toeA_02_loc";
	rename -uid "ACF6D7F8-A54E-6ADA-EDCC-58A8AF68E931";
	setAttr ".t" -type "double3" 0 0 2 ;
createNode locator -n "lt_toeA_03_locShape" -p "lt_toeA_03_loc";
	rename -uid "587F0264-9A43-FABF-BD53-6FBB94D65B1D";
	setAttr -k off ".v";
createNode transform -n "lt_toeB_01_loc" -p "lt_leg_04_loc";
	rename -uid "73613C24-0A47-38A5-D138-9FAA3A1CAB67";
	setAttr ".t" -type "double3" -1.3289189338684082 -2.3190958700070041e-06 2.3269081115722656 ;
createNode locator -n "lt_toeB_01_locShape" -p "lt_toeB_01_loc";
	rename -uid "1587DB91-8F4D-AFA1-7D68-FDB9BC7B09A7";
	setAttr -k off ".v";
createNode transform -n "lt_toeB_02_loc" -p "lt_toeB_01_loc";
	rename -uid "E67389ED-4844-2ADA-99B9-AEB048F0DEF6";
	setAttr ".t" -type "double3" -4.76837158203125e-07 0 1.6888885498046875 ;
createNode locator -n "lt_toeB_02_locShape" -p "lt_toeB_02_loc";
	rename -uid "56D06234-D14B-3937-1D38-B8A9B8444B84";
	setAttr -k off ".v";
createNode transform -n "lt_toeB_03_loc" -p "lt_toeB_02_loc";
	rename -uid "58EA5E3E-A943-2EBA-EA0C-2784CC44E7FE";
	setAttr ".t" -type "double3" 4.76837158203125e-07 0 1.6888895034790039 ;
createNode locator -n "lt_toeB_03_locShape" -p "lt_toeB_03_loc";
	rename -uid "FCF916DB-3F4B-1E75-1C3D-A78AE3933F26";
	setAttr -k off ".v";
createNode transform -n "lt_toeC_01_loc" -p "lt_leg_04_loc";
	rename -uid "FCA35EA2-DE46-D943-8A17-5983203AED97";
	setAttr ".t" -type "double3" 0.20621395111083984 -2.3190958700070041e-06 2.1500406265258789 ;
createNode locator -n "lt_toeC_01_locShape" -p "lt_toeC_01_loc";
	rename -uid "8C5BB1AF-BB44-A32D-02A6-32867DA27437";
	setAttr -k off ".v";
createNode transform -n "lt_toeC_02_loc" -p "lt_toeC_01_loc";
	rename -uid "FA0BF83F-5C47-F30C-CE7E-A481BA679732";
	setAttr ".t" -type "double3" 0 0 1.5888891220092773 ;
createNode locator -n "lt_toeC_02_locShape" -p "lt_toeC_02_loc";
	rename -uid "84B9E1D6-9F46-2680-BFD5-FD88285FB7B6";
	setAttr -k off ".v";
createNode transform -n "lt_toeC_03_loc" -p "lt_toeC_02_loc";
	rename -uid "FFB40035-C543-EEB0-60B2-09BD7CC3042F";
	setAttr ".t" -type "double3" 0 0 1.5888891220092773 ;
createNode locator -n "lt_toeC_03_locShape" -p "lt_toeC_03_loc";
	rename -uid "0D9F7095-3840-E9F7-44D1-7FB275C726B9";
	setAttr -k off ".v";
createNode transform -n "lt_toeD_01_loc" -p "lt_leg_04_loc";
	rename -uid "7F46A53F-B34A-6492-C985-40BA1B26DFFA";
	setAttr ".t" -type "double3" 1.9795465469360352 -2.319095926850423e-06 1.8895940780639648 ;
createNode locator -n "lt_toeD_01_locShape" -p "lt_toeD_01_loc";
	rename -uid "F2C180B9-1541-105A-EE08-F4B616D6EF26";
	setAttr -k off ".v";
createNode transform -n "lt_toeD_02_loc" -p "lt_toeD_01_loc";
	rename -uid "85762BD0-3245-DBE2-FFAD-25A96FF38312";
	setAttr ".t" -type "double3" 0 0 1.3999996185302734 ;
createNode locator -n "lt_toeD_02_locShape" -p "lt_toeD_02_loc";
	rename -uid "8F0D0A1E-0F43-62B1-5464-648FD2EC2D2C";
	setAttr -k off ".v";
createNode transform -n "lt_toeD_03_loc" -p "lt_toeD_02_loc";
	rename -uid "E9E3ED8A-1543-D037-A4B5-4C9E3FBD2F3C";
	setAttr ".t" -type "double3" 0 0 1.4000005722045898 ;
createNode locator -n "lt_toeD_03_locShape" -p "lt_toeD_03_loc";
	rename -uid "ADBCF514-E043-8930-D96F-93BA4E6FDAFA";
	setAttr -k off ".v";
createNode transform -n "lt_toeE_01_loc" -p "lt_leg_04_loc";
	rename -uid "07CC9064-8C49-B062-F406-4089A00BB5DF";
	setAttr ".t" -type "double3" 3.6995162963867188 -2.3190958700070041e-06 1.7239294052124023 ;
createNode locator -n "lt_toeE_01_locShape" -p "lt_toeE_01_loc";
	rename -uid "FE8C8FC1-7B4B-C04E-3D03-77AD94882588";
	setAttr -k off ".v";
createNode transform -n "lt_toeE_02_loc" -p "lt_toeE_01_loc";
	rename -uid "B6C0B2F7-F247-B5F8-DBDD-BFB5556F7949";
	setAttr ".t" -type "double3" 0 0 1.0555562973022461 ;
createNode locator -n "lt_toeE_02_locShape" -p "lt_toeE_02_loc";
	rename -uid "44A25552-C24F-8C40-5967-779B62775376";
	setAttr -k off ".v";
createNode transform -n "lt_toeE_03_loc" -p "lt_toeE_02_loc";
	rename -uid "9E2D61AB-7A41-7A3C-0C9E-4BBF3C498B1A";
	setAttr ".t" -type "double3" 0 0 1.0555553436279297 ;
createNode locator -n "lt_toeE_03_locShape" -p "lt_toeE_03_loc";
	rename -uid "56CCAA36-7A43-17F2-D583-FCABF1E997A4";
	setAttr -k off ".v";
createNode transform -n "ct_back_01_loc" -p "ct_hip_loc";
	rename -uid "EC4B11DB-B449-C52E-2C57-DE9D9D611060";
	setAttr ".t" -type "double3" -1.9808814148442738e-15 3.2609596252441406 -0.15953922271728516 ;
createNode locator -n "ct_back_01_locShape" -p "ct_back_01_loc";
	rename -uid "C9F7B6AF-C141-3236-3A2B-A893BE5BE95C";
	setAttr -k off ".v";
createNode transform -n "ct_back_02_loc" -p "ct_back_01_loc";
	rename -uid "01504B49-884B-89B7-1EAB-66AC22139C93";
	setAttr ".t" -type "double3" 1.1250225960378205e-15 5.0666427612304688 0.0098233222961425781 ;
createNode locator -n "ct_back_02_locShape" -p "ct_back_02_loc";
	rename -uid "A1965AEA-9C4B-5053-40F9-A3BA6196469E";
	setAttr -k off ".v";
createNode transform -n "ct_back_03_loc" -p "ct_back_02_loc";
	rename -uid "E429CBFA-D34F-10D9-65BB-45A08DC1B8A9";
	setAttr ".t" -type "double3" 1.0851959538908705e-15 5.0666427612304688 0.0098235607147216797 ;
createNode locator -n "ct_back_03_locShape" -p "ct_back_03_loc";
	rename -uid "C84FBD53-AC4E-E0B4-4F88-458134B9648B";
	setAttr -k off ".v";
createNode transform -n "ct_back_04_loc" -p "ct_back_03_loc";
	rename -uid "37B83C01-BA49-CC61-406C-FCA1C6F9148C";
	setAttr ".t" -type "double3" 9.1829679372212002e-16 5.0666427612304688 0.0098235607147216797 ;
createNode locator -n "ct_back_04_locShape" -p "ct_back_04_loc";
	rename -uid "E2DF2B1D-7A4E-EA0E-C1C3-8CAA81003F02";
	setAttr -k off ".v";
createNode transform -n "ct_back_05_loc" -p "ct_back_04_loc";
	rename -uid "237B8314-3649-19C2-8275-2C86D2CF3A33";
	setAttr ".t" -type "double3" 7.5139763355336949e-16 5.0666427612304688 0.0098235607147216797 ;
createNode locator -n "ct_back_05_locShape" -p "ct_back_05_loc";
	rename -uid "06486A79-5F4D-68BA-B32F-AC89C9CBED67";
	setAttr -k off ".v";
createNode transform -n "ct_back_06_loc" -p "ct_back_05_loc";
	rename -uid "8A558205-C342-17FE-689D-AEAFB8ED5512";
	setAttr ".t" -type "double3" 7.5139763355336949e-16 5.0666351318359375 0.0098235607147216797 ;
createNode locator -n "ct_back_06_locShape" -p "ct_back_06_loc";
	rename -uid "D8AF65A0-0949-7E70-61C5-1F8644EEE1EA";
	setAttr -k off ".v";
createNode transform -n "ct_back_07_loc" -p "ct_back_06_loc";
	rename -uid "DEB8A02B-6048-4085-2E00-C08E8EAE0719";
	setAttr ".t" -type "double3" 3.4972906189957575e-15 5.4521331787109375 0.41616511344909668 ;
createNode locator -n "ct_back_07_locShape" -p "ct_back_07_loc";
	rename -uid "A0844C20-264A-C4F3-6FCA-C8B9BC0CF6B2";
	setAttr -k off ".v";
createNode transform -n "ct_neck_01_loc" -p "ct_back_07_loc";
	rename -uid "66A36A9A-1244-FD1E-B92F-8994C09FA643";
	setAttr ".t" -type "double3" 8.9846563484452871e-16 1.9993438720702983 0.44633305072784424 ;
createNode locator -n "ct_neck_01_locShape" -p "ct_neck_01_loc";
	rename -uid "98AE5A96-3843-B113-1D9C-84988F62611D";
	setAttr -k off ".v";
createNode transform -n "ct_neck_02_loc" -p "ct_neck_01_loc";
	rename -uid "9AABEA55-BB4C-9F25-DE82-08A82B24B3E1";
	setAttr ".t" -type "double3" 1.1391835046082547e-15 1.52789306640625 0.34638071060180664 ;
createNode locator -n "ct_neck_02_locShape" -p "ct_neck_02_loc";
	rename -uid "40C78AC9-AB44-1912-911D-54A99829D07D";
	setAttr -k off ".v";
createNode transform -n "ct_neck_03_loc" -p "ct_neck_02_loc";
	rename -uid "A16685CB-EF47-B623-2F28-DA8C41BFEF6C";
	setAttr ".t" -type "double3" -4.734688017354622e-15 1.52789306640625 0.34638059139251709 ;
createNode locator -n "ct_neck_03_locShape" -p "ct_neck_03_loc";
	rename -uid "EFC3B17E-0C44-B9EE-18EE-A4AD582B1C14";
	setAttr -k off ".v";
createNode transform -n "ct_neck_04_loc" -p "ct_neck_03_loc";
	rename -uid "39E3FC53-8A4E-28B7-F288-6EAD7DD7F849";
	setAttr ".t" -type "double3" 1.0446194758273637e-15 1.5279083251952983 0.34638234972953791 ;
createNode locator -n "ct_neck_04_locShape" -p "ct_neck_04_loc";
	rename -uid "062D9370-E34A-DDF9-194F-1B979AD970A0";
	setAttr -k off ".v";
createNode transform -n "ct_head_01_loc" -p "ct_neck_04_loc";
	rename -uid "E0D30CF6-1B42-B269-5B25-6E8370C8ECBD";
	setAttr ".t" -type "double3" -6.7069424016311108e-16 2.4697799682617188 1.6199597418308258 ;
createNode locator -n "ct_head_01_locShape" -p "ct_head_01_loc";
	rename -uid "8A179B11-C144-3891-F555-389957D1E540";
	setAttr -k off ".v";
createNode transform -n "ct_head_02_loc" -p "ct_head_01_loc";
	rename -uid "390AF906-A14F-1754-81C8-2194F331545E";
	setAttr ".t" -type "double3" 0 13.819216499928984 1.571867428281994 ;
createNode locator -n "ct_head_02_locShape" -p "ct_head_02_loc";
	rename -uid "6AF9F10D-784F-3BA2-EFA8-25882626F5F1";
	setAttr -k off ".v";
createNode transform -n "lt_eye_01_loc" -p "ct_head_01_loc";
	rename -uid "937E0259-9542-74C3-2F8B-52BE186A0DF7";
	setAttr ".t" -type "double3" 3.3938388824462851 9.1896209716796875 6.8332072496414185 ;
createNode locator -n "lt_eye_01_locShape" -p "lt_eye_01_loc";
	rename -uid "CD3E7817-B748-3BAB-585C-56988BCF068D";
	setAttr -k off ".v";
createNode transform -n "lt_eye_02_loc" -p "lt_eye_01_loc";
	rename -uid "D3C248E7-7148-5F52-B115-45AB7DAC199B";
	setAttr ".t" -type "double3" 0 -0.18930816650390625 6.3560590744018555 ;
createNode locator -n "lt_eye_02_locShape" -p "lt_eye_02_loc";
	rename -uid "AC2B5C3B-214E-EF5B-4E01-9CA14E8C8916";
	setAttr -k off ".v";
createNode transform -n "ct_jaw_01_loc" -p "ct_head_01_loc";
	rename -uid "4401DCA5-FF40-1FD6-8B58-1C85C36E653D";
	setAttr ".t" -type "double3" -3.8246061726714478e-15 4.6320037841796875 4.8791428804397583 ;
createNode locator -n "ct_jaw_01_locShape" -p "ct_jaw_01_loc";
	rename -uid "6EC38646-3D49-4E45-34DE-D1BFBCB6A808";
	setAttr -k off ".v";
createNode transform -n "ct_jaw_02_loc" -p "ct_jaw_01_loc";
	rename -uid "ADB15BB0-034D-00A9-8F0F-18A592A5A1F1";
	setAttr ".t" -type "double3" 0 -2.0000381469726562 5.9999895095825195 ;
createNode locator -n "ct_jaw_02_locShape" -p "ct_jaw_02_loc";
	rename -uid "D2587D99-EC49-773D-C017-759EBD8317E9";
	setAttr -k off ".v";
createNode transform -n "lt_clav_01_loc" -p "ct_back_06_loc";
	rename -uid "C564D45F-C249-AF0A-6479-A083C2BE84AD";
	setAttr ".t" -type "double3" 1.6247329711914036 1.658905029296875 5.863696813583374 ;
createNode locator -n "lt_clav_01_locShape" -p "lt_clav_01_loc";
	rename -uid "4D43D678-4242-A8EC-E996-0F987B65DC1A";
	setAttr -k off ".v";
createNode transform -n "lt_clav_02_loc" -p "lt_clav_01_loc";
	rename -uid "A26A80BF-EC42-F307-52B1-27A13BD836A9";
	setAttr ".t" -type "double3" 5.7373299598693848 0.01202392578125 -5.3403886556625366 ;
createNode locator -n "lt_clav_02_locShape" -p "lt_clav_02_loc";
	rename -uid "AF4FD50D-A24C-15AF-CE77-409EF878DDBF";
	setAttr -k off ".v";
createNode transform -n "lt_arm_01_loc" -p "lt_clav_02_loc";
	rename -uid "97F30867-E842-0FED-1D4F-9F92E6719802";
	setAttr ".t" -type "double3" 1.2079424858093262 1.469329833984375 0 ;
createNode locator -n "lt_arm_01_locShape" -p "lt_arm_01_loc";
	rename -uid "678432B9-6942-7357-5BAF-99915D49E3DB";
	setAttr -k off ".v";
createNode transform -n "lt_arm_02_loc" -p "lt_arm_01_loc";
	rename -uid "C2C1301A-F940-9E21-60EB-C8B2023A4C37";
	setAttr ".t" -type "double3" 16.776611328125 -0.10781097412109375 -2.4519981145858765 ;
createNode locator -n "lt_arm_02_locShape" -p "lt_arm_02_loc";
	rename -uid "D698C0B3-D74D-C9CA-3945-8E9A566609FB";
	setAttr -k off ".v";
createNode transform -n "lt_arm_03_loc" -p "lt_arm_02_loc";
	rename -uid "1E752AE4-5E40-6B9D-DABC-C4A053D4C852";
	setAttr ".t" -type "double3" 13.685880661010742 -0.15152740478515625 3.9556051790714264 ;
createNode locator -n "lt_arm_03_locShape" -p "lt_arm_03_loc";
	rename -uid "0A142F0C-7B47-0063-8851-E9B204A18831";
	setAttr -k off ".v";
createNode transform -n "lt_hand_01_loc" -p "lt_arm_03_loc";
	rename -uid "E3C917DD-E94C-05A4-1C9C-289C1052B258";
	setAttr ".t" -type "double3" 1.1392173767089844 0.6279144287109375 0 ;
createNode locator -n "lt_hand_01_locShape" -p "lt_hand_01_loc";
	rename -uid "7909B49C-B541-4468-5EDB-10951CB3CA4D";
	setAttr -k off ".v";
createNode transform -n "lt_hand_02_loc" -p "lt_hand_01_loc";
	rename -uid "D2818792-AE46-FBC6-2A25-E9ABAC05E79A";
	setAttr ".t" -type "double3" 3.4360885620117188 -0.08823394775390625 0.39120731502771378 ;
createNode locator -n "lt_hand_02_locShape" -p "lt_hand_02_loc";
	rename -uid "A7013B34-334E-7152-463C-549E29863141";
	setAttr -k off ".v";
createNode transform -n "lt_thumb_01_pivot_loc" -p "lt_hand_02_loc";
	rename -uid "07EF60F5-154B-8528-208D-8F989E05DEB0";
	setAttr ".t" -type "double3" -0.47961807250976562 0 2.5963015481829648 ;
createNode locator -n "lt_thumb_01_pivot_locShape" -p "lt_thumb_01_pivot_loc";
	rename -uid "E7A5E270-054A-67C8-6E48-DA99AAAEA46F";
	setAttr -k off ".v";
createNode transform -n "lt_thumb_02_loc" -p "lt_thumb_01_pivot_loc";
	rename -uid "5F2B2A38-EA44-EC9D-55EF-7D905B1EBA3A";
	setAttr ".t" -type "double3" -1.3313522338867188 0 0.56921696662902832 ;
createNode locator -n "lt_thumb_02_locShape" -p "lt_thumb_02_loc";
	rename -uid "EBBCC0C3-284F-FA25-32FE-BFAA81E28755";
	setAttr -k off ".v";
createNode transform -n "lt_thumb_03_loc" -p "lt_thumb_02_loc";
	rename -uid "4D6E3A82-5248-1DF2-8B29-2CB0E853780F";
	setAttr ".t" -type "double3" 0.57981491088867188 -0.70355224609375 0.90447521209716797 ;
createNode locator -n "lt_thumb_03_locShape" -p "lt_thumb_03_loc";
	rename -uid "7E9F99A9-FD45-8235-A51F-0EA39CEFEAB9";
	setAttr -k off ".v";
createNode transform -n "lt_thumb_04_loc" -p "lt_thumb_03_loc";
	rename -uid "2CBB6792-CC48-E694-83E8-93A3BAA9C4D6";
	setAttr ".t" -type "double3" 1.004730224609375 -1.0234527587890625 1.4309954643249512 ;
createNode locator -n "lt_thumb_04_locShape" -p "lt_thumb_04_loc";
	rename -uid "B223EBC6-2D46-DA0A-3BE1-E6813FD717D9";
	setAttr -k off ".v";
createNode transform -n "lt_thumb_05_loc" -p "lt_thumb_04_loc";
	rename -uid "DB2B8B78-714D-3EBA-D158-96BDC1FBAB48";
	setAttr ".t" -type "double3" 1.0657119750976562 -0.96219635009765625 1.4267592430114746 ;
createNode locator -n "lt_thumb_05_locShape" -p "lt_thumb_05_loc";
	rename -uid "A81BB8F6-5D4F-7576-6A7D-A69A2B14ABB7";
	setAttr -k off ".v";
createNode transform -n "lt_middle_01_loc" -p "lt_hand_02_loc";
	rename -uid "4D7C47B2-B044-AF5D-F06D-5C9615DDDE0C";
	setAttr ".t" -type "double3" 1.7852859497070312 0 0.77402292937040329 ;
createNode locator -n "lt_middle_01_locShape" -p "lt_middle_01_loc";
	rename -uid "01BFA208-9C46-7722-25E7-1E8F46AF7229";
	setAttr -k off ".v";
createNode transform -n "lt_middle_02_loc" -p "lt_middle_01_loc";
	rename -uid "C0750640-604A-7736-F429-9090EF042905";
	setAttr ".t" -type "double3" 2.3395805358886719 0 0 ;
createNode locator -n "lt_middle_02_locShape" -p "lt_middle_02_loc";
	rename -uid "2CEE7DA0-1942-7CBC-4189-859F3674FBCF";
	setAttr -k off ".v";
createNode transform -n "lt_middle_03_loc" -p "lt_middle_02_loc";
	rename -uid "8470BC63-DE4D-C7E6-DBD5-05A2C5967A46";
	setAttr ".t" -type "double3" 1.6365547180175781 0 0 ;
createNode locator -n "lt_middle_03_locShape" -p "lt_middle_03_loc";
	rename -uid "F421A001-F948-7BBE-BF72-51A1D4D7C72E";
	setAttr -k off ".v";
createNode transform -n "lt_middle_04_loc" -p "lt_middle_03_loc";
	rename -uid "0615BB91-9246-95D5-4FAC-5794F158D2C2";
	setAttr ".t" -type "double3" 1.6365547180175781 0 0 ;
createNode locator -n "lt_middle_04_locShape" -p "lt_middle_04_loc";
	rename -uid "F76DE927-2F46-A073-4D53-308E5C06FDD5";
	setAttr -k off ".v";
createNode transform -n "lt_middle_05_loc" -p "lt_middle_04_loc";
	rename -uid "41AC095F-9A4D-5CC3-AF3F-199BF4F35939";
	setAttr ".t" -type "double3" 1.5098190307617188 0 0 ;
createNode locator -n "lt_middle_05_locShape" -p "lt_middle_05_loc";
	rename -uid "621A61E0-BD44-BA9B-B714-97A1996DB807";
	setAttr -k off ".v";
createNode transform -n "lt_ring_01_loc" -p "lt_hand_02_loc";
	rename -uid "C4434AE6-524B-16D1-5240-3687CCD9BAC9";
	setAttr ".t" -type "double3" 1.4006881713867188 0 -1.123336561024189 ;
createNode locator -n "lt_ring_01_locShape" -p "lt_ring_01_loc";
	rename -uid "54A76071-EA40-AEA9-9E42-E3A5D190B92A";
	setAttr -k off ".v";
createNode transform -n "lt_ring_02_loc" -p "lt_ring_01_loc";
	rename -uid "77B8A86E-4948-492B-80F3-269CED8A5BE2";
	setAttr ".t" -type "double3" 2.1622314453125 0 0 ;
createNode locator -n "lt_ring_02_locShape" -p "lt_ring_02_loc";
	rename -uid "2AFB4E70-0542-35A0-9C44-1C9F160EAFC1";
	setAttr -k off ".v";
createNode transform -n "lt_ring_03_loc" -p "lt_ring_02_loc";
	rename -uid "7AB2B3DA-B347-D781-2CC7-A88B93D1C625";
	setAttr ".t" -type "double3" 1.5125007629394531 0 0 ;
createNode locator -n "lt_ring_03_locShape" -p "lt_ring_03_loc";
	rename -uid "91BDA824-354C-EAA5-41E6-F1A5424F06EE";
	setAttr -k off ".v";
createNode transform -n "lt_ring_04_loc" -p "lt_ring_03_loc";
	rename -uid "16CBFA19-8747-9BA4-0B8E-759133B5EA93";
	setAttr ".t" -type "double3" 1.5125007629394531 0 0 ;
createNode locator -n "lt_ring_04_locShape" -p "lt_ring_04_loc";
	rename -uid "76F8332A-7442-AD25-6511-A4AF448021D1";
	setAttr -k off ".v";
createNode transform -n "lt_ring_05_loc" -p "lt_ring_04_loc";
	rename -uid "FA7D8C23-BC4D-1637-1A78-AEA06C80D372";
	setAttr ".t" -type "double3" 1.3953704833984375 0 0 ;
createNode locator -n "lt_ring_05_locShape" -p "lt_ring_05_loc";
	rename -uid "76A46D90-ED48-4C9F-12C8-C9B7AFD322D3";
	setAttr -k off ".v";
createNode transform -n "lt_pinky_01_loc" -p "lt_hand_02_loc";
	rename -uid "09C4204C-494E-B50D-C0A8-DA8CAED080BD";
	setAttr ".t" -type "double3" 0.9135284423828125 0 -2.7899358347058296 ;
createNode locator -n "lt_pinky_01_locShape" -p "lt_pinky_01_loc";
	rename -uid "F7C11E13-8749-F361-0F4E-A8BA79640F35";
	setAttr -k off ".v";
createNode transform -n "lt_pinky_02_loc" -p "lt_pinky_01_loc";
	rename -uid "0A6F4AD9-5244-71E2-35C6-7EAE773BCA53";
	setAttr ".t" -type "double3" 1.9339942932128906 0 0 ;
createNode locator -n "lt_pinky_02_locShape" -p "lt_pinky_02_loc";
	rename -uid "69C76E91-A942-5D07-689E-13A22731EEB0";
	setAttr -k off ".v";
createNode transform -n "lt_pinky_03_loc" -p "lt_pinky_02_loc";
	rename -uid "73872AF4-4443-C71C-E8CF-458AB007FC18";
	setAttr ".t" -type "double3" 1.3528480529785156 0 0 ;
createNode locator -n "lt_pinky_03_locShape" -p "lt_pinky_03_loc";
	rename -uid "C552F690-4143-8C11-0135-9F984E85231F";
	setAttr -k off ".v";
createNode transform -n "lt_pinky_04_loc" -p "lt_pinky_03_loc";
	rename -uid "9C0E4276-1A41-8230-762A-2B8AFD2B721A";
	setAttr ".t" -type "double3" 1.3528480529785156 0 0 ;
createNode locator -n "lt_pinky_04_locShape" -p "lt_pinky_04_loc";
	rename -uid "8A8F2B94-1B4F-B895-1CB4-19B0102EE7D4";
	setAttr -k off ".v";
createNode transform -n "lt_pinky_05_loc" -p "lt_pinky_04_loc";
	rename -uid "75124110-1446-692F-A6E0-03B5CDF456CB";
	setAttr ".t" -type "double3" 1.2480812072753906 0 0 ;
createNode locator -n "lt_pinky_05_locShape" -p "lt_pinky_05_loc";
	rename -uid "A859A4DC-F545-D108-F21E-829C381087D5";
	setAttr -k off ".v";
createNode transform -n "lt_index_01_loc" -p "lt_hand_02_loc";
	rename -uid "D5C83B32-844F-026E-B519-9B936E3A2607";
	setAttr ".t" -type "double3" 1.298126220703125 0 2.6457424089312553 ;
createNode locator -n "lt_index_01_locShape" -p "lt_index_01_loc";
	rename -uid "8B9F3B3C-1048-E143-7CB6-648909A0A200";
	setAttr -k off ".v";
createNode transform -n "lt_index_02_loc" -p "lt_index_01_loc";
	rename -uid "533576E8-F648-C25F-D804-35BF73DDA569";
	setAttr ".t" -type "double3" 2.3587989807128906 0 0 ;
createNode locator -n "lt_index_02_locShape" -p "lt_index_02_loc";
	rename -uid "27F8FD54-E747-FE0B-CBBE-898AF5F4DF18";
	setAttr -k off ".v";
createNode transform -n "lt_index_03_loc" -p "lt_index_02_loc";
	rename -uid "FBAE115F-C541-F451-3698-D29977B4371C";
	setAttr ".t" -type "double3" 1.6500015258789062 0 0 ;
createNode locator -n "lt_index_03_locShape" -p "lt_index_03_loc";
	rename -uid "C86D81DD-674D-FAB0-1DFB-CE80A5EE81DA";
	setAttr -k off ".v";
createNode transform -n "lt_index_04_loc" -p "lt_index_03_loc";
	rename -uid "3DC65CD9-1144-39AF-8F6D-5A82ECD01AB6";
	setAttr ".t" -type "double3" 1.6500015258789062 0 0 ;
createNode locator -n "lt_index_04_locShape" -p "lt_index_04_loc";
	rename -uid "009B669A-6544-DC56-4EF8-D4B47C473D4C";
	setAttr -k off ".v";
createNode transform -n "lt_index_05_loc" -p "lt_index_04_loc";
	rename -uid "0D4E6AD1-964C-AE3A-649D-B1831951D002";
	setAttr ".t" -type "double3" 1.5222206115722656 0 0 ;
createNode locator -n "lt_index_05_locShape" -p "lt_index_05_loc";
	rename -uid "D2E53940-294F-E38E-39F6-9D9105A28FE8";
	setAttr -k off ".v";
createNode transform -n "icon_grp" -p "fitSkeleton_crv";
	rename -uid "E494B532-8E40-440D-F773-5BA7A9DED45B";
createNode transform -n "lt_leg_01_fk_icon" -p "icon_grp";
	rename -uid "33440292-6942-44FF-7181-3099F3D8C01F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 5.8907906424362473 5.8907906424362473 5.8907906424362473 ;
	setAttr ".rp" -type "double3" 7.7717790603637775 45.971321105957024 -2.2663607597351119 ;
	setAttr ".sp" -type "double3" 1.3193100098274095 7.8039305581134553 -0.38472946965873056 ;
	setAttr ".spt" -type "double3" 6.4524690505363678 38.167390547843567 -1.8816312900763794 ;
createNode nurbsCurve -n "lt_leg_01_fk_iconShape" -p "lt_leg_01_fk_icon";
	rename -uid "46E70FB3-FE4F-F316-E99B-C5A993F723BF";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "lt_leg_01_fk_icon_parentConstraint1" -p "lt_leg_01_fk_icon";
	rename -uid "A274D561-9C42-BDE7-AAB7-5C920A677109";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 8.8817841970012523e-15 -7.1054273576010019e-15 
		-4.8849813083506888e-15 ;
	setAttr ".rst" -type "double3" 8.8817841970012523e-16 0 -4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_leg_02_fk_icon" -p "icon_grp";
	rename -uid "CF73530A-3249-F042-2012-FA81C1BCC382";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 6.1960716096857613 6.1960716096857613 6.1960716096857613 ;
	setAttr ".rp" -type "double3" 7.7717790603637802 23.924690246582045 1.6649701595306401 ;
	setAttr ".sp" -type "double3" 1.2543074951255981 3.8612675504238405 0.2687138342507116 ;
	setAttr ".spt" -type "double3" 6.5174715652381821 20.063422696158202 1.3962563252799278 ;
createNode nurbsCurve -n "lt_leg_02_fk_iconShape" -p "lt_leg_02_fk_icon";
	rename -uid "DB474114-634A-13DC-1B3E-87B98FFA3A85";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.0379191200168236 3.7384986629501951 1.0426485724122359
		1.2543074951255981 3.6876461247211538 1.3632228373504105
		0.4706958702343737 3.7384986629501942 1.042648572412237
		0.14611330757120952 3.8612675504238401 0.2687138342507126
		0.47069587023437254 3.9840364378974864 -0.50522090391081242
		1.2543074951255966 4.0348889761265276 -0.82579516884898718
		2.0379191200168214 3.9840364378974873 -0.50522090391081331
		2.3625016826799858 3.8612675504238414 0.26871383425071071
		2.0379191200168236 3.7384986629501951 1.0426485724122359
		1.2543074951255981 3.6876461247211538 1.3632228373504105
		0.4706958702343737 3.7384986629501942 1.042648572412237
		;
createNode parentConstraint -n "lt_leg_02_fk_icon_parentConstraint1" -p "lt_leg_02_fk_icon";
	rename -uid "02ECE296-0C49-0180-F36F-6F815A967928";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.9936057773011271e-15 7.1054273576010019e-15 
		2.2204460492503131e-16 ;
	setAttr ".rst" -type "double3" -2.6645352591003757e-15 -7.1054273576010019e-15 -2.2204460492503131e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_leg_03_fk_icon" -p "icon_grp";
	rename -uid "338F1632-1348-2B71-C99F-3E8C26D1FF0F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 5.2346619779748629 5.2346619779748629 5.2346619779748629 ;
	setAttr ".rp" -type "double3" 7.7717790603637686 5.2744808197021626 -1.2935034036636326 ;
	setAttr ".sp" -type "double3" 1.4846763922988671 1.0076067646573628 -0.24710352055321269 ;
	setAttr ".spt" -type "double3" 6.2871026680649038 4.2668740550448003 -1.0463998831104198 ;
createNode nurbsCurve -n "lt_leg_03_fk_iconShape" -p "lt_leg_03_fk_icon";
	rename -uid "B0DEA38F-E84C-4E38-83AB-B094461E9BC6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.2682880171900917 1.714287685499265 0.091495438072925817
		1.4846763922988659 2.0070045071822888 0.23174771894127949
		0.70106476740764201 1.7142876854992644 0.091495438072926386
		0.37648220474447891 1.0076067646573621 -0.2471035205532123
		0.70106476740764267 0.30092584381545984 -0.58570247917935103
		1.4846763922988668 0.008209022132436199 -0.72595476004770465
		2.2682880171900912 0.30092584381546056 -0.58570247917935159
		2.5928705798532548 1.0076067646573625 -0.24710352055321308
		2.2682880171900917 1.714287685499265 0.091495438072925817
		1.4846763922988659 2.0070045071822888 0.23174771894127949
		0.70106476740764201 1.7142876854992644 0.091495438072926386
		;
createNode parentConstraint -n "lt_leg_03_fk_icon_parentConstraint1" -p "lt_leg_03_fk_icon";
	rename -uid "64585DAD-9E44-25AF-A0C5-1480076591DE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.7763568394002505e-15 1.4210854715202004e-14 
		2.886579864025407e-15 ;
	setAttr ".rst" -type "double3" -8.8817841970012523e-16 0 2.2204460492503131e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_leg_04_fk_icon" -p "icon_grp";
	rename -uid "985E5AD9-984E-542F-D200-DF9447DF57A9";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 5.1139247951928848 5.1139247951928848 5.1139247951928848 ;
	setAttr ".rp" -type "double3" 7.7717790603637766 1.542665250653386e-06 9.7147226333618253 ;
	setAttr ".sp" -type "double3" 1.5197288524206081 3.0165974519287008e-07 1.89966083241852 ;
	setAttr ".spt" -type "double3" 6.2520502079431681 1.2410055054605157e-06 7.8150618009433055 ;
createNode nurbsCurve -n "lt_leg_04_fk_iconShape" -p "lt_leg_04_fk_icon";
	rename -uid "E84B094F-5B42-9C80-AAAD-F7BB4CEA69A5";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		2.3033404211169923 0.78361198274576582 1.8996605850855561
		1.5197287729491606 1.10819448921413 1.8996608324185447
		0.73611717133462573 0.78361187035616853 1.8996610797515188
		0.41153466486627804 2.221882988118567e-07 1.8996611822001763
		0.73611728372422336 -0.78361137942627557 1.8996610797514832
		1.5197289318920537 -1.1081938858946399 1.8996608324184945
		2.3033405335065886 -0.78361126703667816 1.8996605850855206
		2.6279230399749376 3.8113119129979699e-07 1.899660482636863
		2.3033404211169923 0.78361198274576582 1.8996605850855561
		1.5197287729491606 1.10819448921413 1.8996608324185447
		0.73611717133462573 0.78361187035616853 1.8996610797515188
		;
createNode parentConstraint -n "lt_leg_04_fk_icon_parentConstraint1" -p "lt_leg_04_fk_icon";
	rename -uid "5780C365-6E45-F378-FCF8-3E90AD4F2ACC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 9.7699626167013776e-15 5.329070941717225e-15 
		5.3290705182007514e-15 ;
	setAttr ".rst" -type "double3" 2.6645352591003757e-15 0 -3.5527136788005009e-15 ;
	setAttr -k on ".w0";
createNode transform -n "ct_eyes_icon" -p "icon_grp";
	rename -uid "21FD04A8-4941-BD1F-09F2-D38AB1EB85E9";
	addAttr -ci true -sn "FollowHead" -ln "FollowHead" -min 0 -max 1 -at "bool";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr -k on ".FollowHead";
createNode nurbsCurve -n "ct_eyes_iconShape" -p "ct_eyes_icon";
	rename -uid "DBA4C75C-CA4D-9B84-E510-788EF8C6FD1C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
	setAttr -s 11 ".cp[1:10]" -type "double3" 9.8607613152626476e-32 6.1836247895144822 
		-3.5527136788005009e-15 0 0 0 1.8879578662105265 0 0 0 0 0 -3.9443045261050599e-31 
		-6.1836247895144822 3.5527136788005009e-15 0 0 0 -1.8879578662105265 0 0 0 0 0 0 
		0 0 0 0 0;
createNode transform -n "rt_eye_icon" -p "ct_eyes_icon";
	rename -uid "982CC607-674E-D058-C5A8-E29724A6F211";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".rp" -type "double3" -3 0 0 ;
	setAttr ".sp" -type "double3" -3 0 0 ;
createNode nurbsCurve -n "rt_eye_iconShape" -p "rt_eye_icon";
	rename -uid "8237A991-6F49-F269-ACFC-ACB02B2A691C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "lt_eye_icon" -p "ct_eyes_icon";
	rename -uid "EF197C6A-6447-C34E-1649-27AECBECC00B";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" -8.8817841970012523e-16 0 3.5527136788005009e-15 ;
	setAttr ".rp" -type "double3" 3 0 0 ;
	setAttr ".sp" -type "double3" 3 0 0 ;
createNode nurbsCurve -n "lt_eye_iconShape" -p "lt_eye_icon";
	rename -uid "F76DB2E4-B244-29A5-A7BD-BEB60BCEFC08";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_eyes_icon_parentConstraint1" -p "ct_eyes_icon";
	rename -uid "4B862E90-DE43-BB73-F421-1CB925150B4D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_eye_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -3.3938388824462891 4.2632564145606011e-14 
		23.65819628784849 ;
	setAttr ".rst" -type "double3" 0 100.25115966796876 31.718500929572123 ;
	setAttr -k on ".w0";
createNode transform -n "ct_jaw_icon" -p "icon_grp";
	rename -uid "4128F770-254E-D88D-BEC0-37AEEEC78B09";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 1.4427907487048335 1.4427907487048335 1.4427907487048335 ;
	setAttr ".rp" -type "double3" 4.9960036108132044e-16 5.7067236534941754 -10.642489240301519 ;
	setAttr ".sp" -type "double3" 0 3.9553370151679985 -7.3763220687789177 ;
	setAttr ".spt" -type "double3" 4.9960036108132044e-16 1.7513866383261767 -3.2661671715225999 ;
createNode nurbsCurve -n "ct_jaw_iconShape" -p "ct_jaw_icon";
	rename -uid "1BBDDCE0-5A4A-2C16-479F-16A153B81A00";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 0 no 3
		21 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16 16
		19
		-3 2 0
		-2 2 0
		-2 2 0
		-2 2 0
		0 -0.5 0.5
		2 2 0
		2 2 0
		2 2 0
		3 2 0
		3 2 0
		3 2 0
		3 2 0
		0.5 0 0.5
		0 -2 3.5527136788005009e-15
		0 -2 3.5527136788005009e-15
		0 -2 3.5527136788005009e-15
		0 -2 3.5527136788005009e-15
		-0.5 0 0.5
		-3 2 0
		;
createNode parentConstraint -n "ct_jaw_icon_parentConstraint1" -p "ct_jaw_icon";
	rename -uid "3F598B03-4240-B884-05F8-8699F1891EC1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_jaw_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 2.3980817331903381e-14 -3.5527136788005009e-15 ;
	setAttr ".rst" -type "double3" -4.9960036108132044e-16 89.98681882697457 16.748729512823488 ;
	setAttr -k on ".w0";
createNode transform -n "lt_foot_icon" -p "icon_grp";
	rename -uid "3685F1E3-854A-75E5-9F59-C5BB38384A06";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 6.7006280869980852 6.7006280869980852 6.7006280869980852 ;
	setAttr ".rp" -type "double3" 7.771779060363766 8.8817841970012523e-16 6.3873970038082835 ;
	setAttr ".sp" -type "double3" 1.1598582937984796 0 0.95325347428286666 ;
	setAttr ".spt" -type "double3" 6.6119207665652864 8.8817841970012523e-16 5.434143529525417 ;
createNode nurbsCurve -n "curveShape1" -p "lt_foot_icon";
	rename -uid "11F69A03-A24A-5585-EE09-39AA7A799BDB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 38 0 no 3
		43 0 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
		 26 27 28 29 30 31 32 33 34 35 36 37 38 38 38
		41
		1.1598566195784796 0 3.1047799742828666
		1.0256982937984795 0 3.0852749742828665
		0.89307929379847961 0 3.0173839742828665
		0.76438629379847955 0 2.9199249742828663
		0.64086529379847956 0 2.7804869742828666
		0.52336229379847965 0 2.6011229742828665
		0.42222629379847965 0 2.3738789742828663
		0.34038429379847956 0 2.0882999742828665
		0.31371429379847959 0 1.7432419742828664
		0.33525629379847965 0 1.4779829742828663
		0.41065229379847956 0 1.0890679742828664
		0.48620229379847957 0 0.79461797428286651
		0.56205029379847959 0 0.5022679742828664
		0.61480429379847956 0 0.17575097428286646
		0.61496729379847959 0 -0.17536202571713366
		0.58795429379847963 0 -0.52643902571713352
		0.64757929379847956 0 -0.83158002571713363
		0.76658729379847967 0 -1.0012050257171334
		0.89301929379847955 0 -1.1138920257171336
		1.0258932937984797 0 -1.1758760257171335
		1.1598582937984796 0 -1.1982730257171332
		1.2938232937984795 0 -1.1758760257171335
		1.4266972937984796 0 -1.1138920257171336
		1.5531292937984795 0 -1.0012050257171334
		1.6721372937984795 0 -0.83158002571713363
		1.7317622937984796 0 -0.52643902571713352
		1.7047492937984796 0 -0.17536202571713366
		1.7049122937984795 0 0.17575097428286646
		1.7576652937984796 0 0.50226897428286643
		1.8335142937984796 0 0.79461797428286651
		1.9090652937984796 0 1.0890689742828665
		1.9844602937984797 0 1.4779829742828663
		2.0060022937984794 0 1.7432449742828664
		1.9793322937984796 0 2.0883019742828663
		1.8974892937984795 0 2.3738839742828666
		1.7963442937984797 0 2.6011219742828664
		1.6788662937984795 0 2.7804959742828665
		1.5553622937984797 0 2.9199549742828665
		1.4264542937984797 0 3.0173049742828666
		1.2941512937984796 0 3.0853039742828665
		1.1598566195784796 0 3.1047799742828666
		;
createNode nurbsCurve -n "curveShape2" -p "lt_foot_icon";
	rename -uid "00DFA98F-6E40-EAFC-84E2-3D82859BB493";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 3 0 no 3
		8 0 0 0 1 2 3 3 3
		6
		0.61496729379847959 0 -0.17536202571713366
		0.61496729379847959 0 -0.17536202571713366
		0.61496729379847959 0 -0.17536202571713366
		1.7047492937984796 0 -0.17536202571713366
		1.7047492937984796 0 -0.17536202571713366
		1.7047492937984796 0 -0.17536202571713366
		;
createNode parentConstraint -n "lt_foot_icon_parentConstraint1" -p "lt_foot_icon";
	rename -uid "7DF76FB4-DD43-1382-D2B7-0E8C7199372A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -4.4408920985006262e-15 -5.2744808197021475 
		7.6809004074719178 ;
	setAttr ".rst" -type "double3" -8.8817841970012523e-16 0 -8.8817841970012523e-16 ;
	setAttr -k on ".w0";
createNode transform -n "ct_hip_icon" -p "icon_grp";
	rename -uid "63BAA837-1440-6FF2-4432-D593099C41BD";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".s" -type "double3" 13.63238207431815 3.2555554952418193 12.181904054348879 ;
	setAttr ".rp" -type "double3" 0 47.962421417236314 -2.1840825080871582 ;
	setAttr ".sp" -type "double3" 0 14.732484667312887 -0.17928909129008053 ;
	setAttr ".spt" -type "double3" 0 33.229936749923425 -2.0047934167970776 ;
createNode nurbsCurve -n "ct_hip_iconShape" -p "ct_hip_icon";
	rename -uid "F6638028-9648-600F-6AF1-31A3734ED8FF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		0.99999999999999978 14.732484628514245 0.82071090870991947
		0.99999999999999978 14.732484628514245 -1.1792890912900806
		-0.99999999999999978 14.732484628514245 -1.1792890912900806
		-0.99999999999999978 14.732484628514245 0.82071090870991947
		0.99999999999999978 14.732484628514245 0.82071090870991947
		0.60000001069603126 12.732484628514245 0.43182201318809876
		0.60000001069603126 12.732484628514245 -0.79040019576825982
		0.99999999999999978 14.732484628514245 -1.1792890912900806
		-0.99999999999999978 14.732484628514245 -1.1792890912900806
		-0.60000001069603126 12.732484628514245 -0.79040019576825982
		0.60000001069603126 12.732484628514245 -0.79040019576825982
		-0.60000001069603126 12.732484628514245 -0.79040019576825982
		-0.60000001069603126 12.732484628514245 0.43182201318809876
		-0.99999999999999978 14.732484628514245 0.82071090870991947
		-0.60000001069603126 12.732484628514245 0.43182201318809876
		0.60000001069603126 12.732484628514245 0.43182201318809876
		;
createNode parentConstraint -n "ct_hip_icon_parentConstraint1" -p "ct_hip_icon";
	rename -uid "D09CCD3B-F944-2F7A-A8BF-47A748AB9850";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_hip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -2.1316282072803006e-14 0 ;
	setAttr ".rst" -type "double3" 0 -7.1054273576010019e-15 0 ;
	setAttr -k on ".w0";
createNode transform -n "ct_back_icon" -p "icon_grp";
	rename -uid "6FB5051D-B841-1940-7E52-5196D09BD6A9";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".s" -type "double3" 13.63238207431815 3.2555554952418193 12.181904054348879 ;
	setAttr ".rp" -type "double3" -3.1554436208840469e-30 51.223381042480455 -2.1840825080871582 ;
	setAttr ".sp" -type "double3" -2.3146678281769569e-31 15.734144639016709 -0.17928909129008053 ;
	setAttr ".spt" -type "double3" -2.9239768380663513e-30 35.48923640346375 -2.0047934167970776 ;
createNode nurbsCurve -n "ct_back_iconShape" -p "ct_back_icon";
	rename -uid "C633B9B9-A242-BF58-C7D8-BDA345C2BCF9";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-0.99999999999999956 15.079862377535285 0.82071090870991947
		-0.99999999999999956 15.079862377535285 -1.1792890912900806
		0.99999999999999944 15.079862377535285 -1.1792890912900806
		0.99999999999999944 15.079862377535285 0.82071090870991947
		-0.99999999999999956 15.079862377535285 0.82071090870991947
		-0.8000000038556021 17.079862377535285 0.60836522415960259
		-0.8000000038556021 17.079862377535285 -0.96694340673976364
		-0.99999999999999956 15.079862377535285 -1.1792890912900806
		0.99999999999999944 15.079862377535285 -1.1792890912900806
		0.80000000385560155 17.079862377535285 -0.96694340673976364
		-0.8000000038556021 17.079862377535285 -0.96694340673976364
		0.80000000385560155 17.079862377535285 -0.96694340673976364
		0.80000000385560155 17.079862377535285 0.60836522415960259
		0.99999999999999944 15.079862377535285 0.82071090870991947
		0.80000000385560155 17.079862377535285 0.60836522415960259
		-0.8000000038556021 17.079862377535285 0.60836522415960259
		;
createNode parentConstraint -n "ct_back_icon_parentConstraint1" -p "ct_back_icon";
	rename -uid "C89EC3CE-D24D-AFCE-E3F4-018206D3F890";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_back_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.9808814148442707e-15 -2.1316282072803006e-14 
		0.15953922271728516 ;
	setAttr ".rst" -type "double3" -3.5032461608120427e-46 -7.1054273576010019e-15 0 ;
	setAttr -k on ".w0";
createNode transform -n "ct_COG_icon" -p "icon_grp";
	rename -uid "170E5A7C-1E4F-ADAF-C9DA-609DB5BCC1B2";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 29.787962420567904 29.787962420567904 29.787962420567904 ;
	setAttr ".rp" -type "double3" 0 47.962421417236328 -2.1840825080871582 ;
	setAttr ".sp" -type "double3" 0 47.962421417236328 -2.1840825080871582 ;
createNode nurbsCurve -n "ct_COG_iconShape" -p "ct_COG_icon";
	rename -uid "80B9F2ED-6344-2DCC-82A0-5EB8B4314FF5";
	setAttr -k off ".v";
	setAttr ".tw" yes;
	setAttr -s 19 ".cp[0:18]" -type "double3" 0 0.019180288069144069 0 
		-1.7026639569035014e-16 0.019180288069144069 0.71822384494628411 0 0.019180288069144069 
		0 0.50786095117139318 0.019180288069144069 0.50786095117139318 0 0.019180288069144069 
		0 0.71822384494628433 0.019180288069144069 0 0 0.019180288069144069 0 0.50786095117139318 
		0.019180288069144069 -0.50786095117139318 0 0.019180288069144069 0 -5.4275939989544642e-17 
		0.019180288069144069 -0.71822384494628411 0 0.019180288069144069 0 -0.50786095117139296 
		0.019180288069144069 -0.50786095117139274 0 0.019180288069144069 0 -0.71822384494628388 
		0.019180288069144069 0 0 0.019180288069144069 0 -0.50786095117139296 0.019180288069144069 
		0.50786095117139318 0 0 0 0 0 0 0 0 0;
createNode parentConstraint -n "ct_COG_icon_parentConstraint1" -p "ct_COG_icon";
	rename -uid "6DDB6302-F545-2E44-1BA6-B192FF5D5DAB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_hip_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 2.2737367544323206e-13 -1.4210854715202004e-14 ;
	setAttr ".rst" -type "double3" 0 2.2737367544323206e-13 -1.4210854715202004e-14 ;
	setAttr -k on ".w0";
createNode transform -n "ct_back_01_fk_icon" -p "icon_grp";
	rename -uid "9D0EE442-BB4F-7058-B1BC-DAB0EAF9AEAC";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 10.886187169843975 10.886187169843975 10.886187169843975 ;
	setAttr ".rp" -type "double3" -2.8421709430403979e-14 61.356666564941399 -2.3239748477935827 ;
	setAttr ".sp" -type "double3" -2.6108047736984967e-15 5.63619434496833 -0.21347922936978958 ;
	setAttr ".spt" -type "double3" -2.5810904656705478e-14 55.720472219973075 -2.1104956184237929 ;
createNode nurbsCurve -n "ct_back_01_fk_iconShape" -p "ct_back_01_fk_icon";
	rename -uid "6B5702AF-0141-8826-D9E5-9ABA0D54E7F6";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_back_01_fk_icon_parentConstraint1" -p "ct_back_01_fk_icon";
	rename -uid "5F4F6B01-5346-7A72-6086-C8805E3F9850";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_back_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -2.8651046565488399e-14 0 -3.5527136788005009e-15 ;
	setAttr ".rst" -type "double3" -3.1554436208840472e-30 7.1054273576010019e-15 0 ;
	setAttr -k on ".w0";
createNode transform -n "ct_back_02_fk_icon" -p "icon_grp";
	rename -uid "D38B000D-744C-B353-1479-B195BADE2DBE";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".s" -type "double3" 10.886187169843975 10.886187169843975 10.886187169843975 ;
	setAttr ".rp" -type "double3" -2.8421709430403973e-14 71.48995208740233 -2.3239748477935813 ;
	setAttr ".sp" -type "double3" -2.6108047736984955e-15 6.5670331560565067 -0.2134792293697895 ;
	setAttr ".spt" -type "double3" -2.5810904656705471e-14 64.922918931345833 -2.110495618423792 ;
createNode nurbsCurve -n "ct_back_02_fk_iconShape" -p "ct_back_02_fk_icon";
	rename -uid "2DEF2F13-5A42-8728-F710-6B8CB5C8306A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78512945168226367 6.5655168233624632 0.56861015309592144
		1.108192104640062 6.5670373218308127 -0.21562783947898911
		0.7820908524144945 6.5685553800450736 -0.99860720539218573
		-0.0021486141475497477 6.5691817400918033 -1.3216692511499979
		-0.78512945168226744 6.5685494887505564 -0.99556861183550049
		-1.1081921046400662 6.567028990282207 -0.21133061926058283
		-0.78209085241449827 6.5655109320679461 0.57164874665260679
		0.0021486141475459924 6.5648845720212163 0.89471079241042573
		0.78512945168226367 6.5655168233624632 0.56861015309592144
		1.108192104640062 6.5670373218308127 -0.21562783947898911
		0.7820908524144945 6.5685553800450736 -0.99860720539218573
		;
createNode parentConstraint -n "ct_back_02_fk_icon_parentConstraint1" -p "ct_back_02_fk_icon";
	rename -uid "C48368F8-BD44-B294-E41D-7DAB7DF21509";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_back_05_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -3.0320740992763876e-14 -1.4210854715202004e-14 
		-0.019647121429446024 ;
	setAttr ".rst" -type "double3" 3.1554436208840472e-30 0 -4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_shoulder_icon" -p "icon_grp";
	rename -uid "63CEC443-BB4F-66A4-85B6-9EA3D596201D";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 3.0875354363731078 3.0875354363731078 3.0875354363731078 ;
	setAttr ".sp" -type "double3" 1.1506632885722707e-15 4.6026531542890827e-15 -2.1574936660730076e-16 ;
	setAttr ".spt" -type "double3" 2.4020503902282305e-15 9.6082015609129218e-15 -4.5038444816779316e-16 ;
createNode nurbsCurve -n "lt_shoulder_iconShape" -p "lt_shoulder_icon";
	rename -uid "47894F80-9849-5DED-8029-468D9E077015";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 22 0 no 3
		23 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
		23
		-0.64264487555906635 -0.77038174247754299 0
		0.51358757235246832 -0.42842970351517806 -2.2204460492503131e-16
		0.25679417012502315 -0.21421517204390028 -2.2204460492503131e-16
		0.36390175614696263 -0.085818086981394259 -2.2204460492503131e-16
		0.57811628761823242 0.17097531524605358 -2.2204460492503131e-16
		0.89943904568407129 0.55616657043359652 -4.4408920985006262e-16
		0.38585070543400191 0.98459691452139353 -4.4408920985006262e-16
		0.064527947368158589 0.59940565933381862 -2.2204460492503131e-16
		-0.1496865841031112 0.34261225710637078 -2.2204460492503131e-16
		-0.25679417012505157 0.21421517204386831 -2.2204460492503131e-16
		-0.5135875723524963 0.42842970351514253 -2.2204460492503131e-16
		-0.64264487555906635 -0.77038174247754299 0
		-1.3766765505351941e-14 -1.7763568394002505e-14 0.66882299999999972
		-1.3766765505351941e-14 -1.7763568394002505e-14 0.33441199999999971
		0.10710758602192616 0.12839708506249181 0.33441199999999971
		0.3213221174931955 0.38519048728993255 0.33441199999999971
		0.64264487555903616 0.77038174247749325 0.33441199999999949
		0.64264487555903616 0.77038174247749325 -0.33441200000000038
		0.3213221174931955 0.38519048728993255 -0.33441200000000038
		0.10710758602192616 0.12839708506249181 -0.33441200000000038
		-1.3766765505351941e-14 -1.7763568394002505e-14 -0.33441200000000038
		-1.3766765505351941e-14 -1.7763568394002505e-14 -0.66882300000000072
		-0.64264487555906635 -0.77038174247754299 0
		;
createNode parentConstraint -n "lt_shoulder_icon_parentConstraint1" -p "lt_shoulder_icon";
	rename -uid "F1E36708-C845-60AF-8C0F-2599010447CA";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_clav_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 10.335896062617961 10.526749454943214 -5.3403886556625375 ;
	setAttr ".rst" -type "double3" 11.960629033809367 88.742241703478371 -1.7711960077285775 ;
	setAttr -k on ".w0";
createNode transform -n "ct_chest_icon" -p "icon_grp";
	rename -uid "31145140-0843-366C-05F1-FFA532BFF783";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".s" -type "double3" 13.63238207431815 3.2555554952418193 12.181904054348879 ;
	setAttr ".rp" -type "double3" 6.1477198149090338e-15 82.008720397949219 -1.8783390522003174 ;
	setAttr ".sp" -type "double3" 4.5096445957824461e-16 25.190392397798057 -0.15419092481932328 ;
	setAttr ".spt" -type "double3" 5.696755355330789e-15 56.818328000151155 -1.7241481273809942 ;
createNode nurbsCurve -n "ct_chest_iconShape" -p "ct_chest_icon";
	rename -uid "E983DB2F-C14E-3A05-261C-FBAF66DD2902";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		-0.99999999999999856 21.142360421992755 0.84580907518067683
		-0.99999999999999856 21.142360421992755 -1.1541909248193234
		0.99999999999999956 21.142360421992755 -1.1541909248193234
		0.99999999999999956 21.142360421992755 0.84580907518067683
		-0.99999999999999856 21.142360421992755 0.84580907518067683
		-0.50666665002873645 24.904762006875423 0.44967738746054708
		-0.50666665002873645 24.904762006875423 -0.75805923709919365
		-0.99999999999999856 21.142360421992755 -1.1541909248193234
		0.99999999999999956 21.142360421992755 -1.1541909248193234
		0.50666665002873701 24.904762006875423 -0.75805923709919365
		-0.50666665002873645 24.904762006875423 -0.75805923709919365
		0.50666665002873701 24.904762006875423 -0.75805923709919365
		0.50666665002873701 24.904762006875423 0.44967738746054708
		0.99999999999999956 21.142360421992755 0.84580907518067683
		0.50666665002873701 24.904762006875423 0.44967738746054708
		-0.50666665002873645 24.904762006875423 0.44967738746054708
		;
createNode parentConstraint -n "ct_chest_icon_parentConstraint1" -p "ct_chest_icon";
	rename -uid "3D93785A-114E-6891-5F37-CE8E3BB81383";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_back_07_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.8886090522101181e-31 0 0 ;
	setAttr ".rst" -type "double3" -7.8886090522101181e-31 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_arm_icon" -p "icon_grp";
	rename -uid "A82FE205-8E41-4C41-155A-D29F6C88B15F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 3.1621534476433468 3.1621534476433468 3.1621534476433468 ;
	setAttr ".rp" -type "double3" 39.032497406005859 79.437507629394531 -0.26758894324302673 ;
	setAttr ".sp" -type "double3" 12.343644308310068 25.121332327688521 -0.084622377652941644 ;
	setAttr ".spt" -type "double3" 26.688853097695791 54.316175301705997 -0.18296656559008506 ;
createNode nurbsCurve -n "lt_arm_iconShape" -p "lt_arm_icon";
	rename -uid "BB62F736-114F-2146-DE04-77955D449DE1";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		13.343644308310068 26.121332327688521 0.91537762234705833
		13.343644308310068 26.121332327688521 -1.0846223776529416
		11.343644308310068 26.121332327688521 -1.0846223776529416
		11.343644308310068 26.121332327688521 0.91537762234705833
		13.343644308310068 26.121332327688521 0.91537762234705833
		13.343644308310068 24.121332327688521 0.91537762234705833
		13.343644308310068 24.121332327688521 -1.0846223776529416
		13.343644308310068 26.121332327688521 -1.0846223776529416
		11.343644308310068 26.121332327688521 -1.0846223776529416
		11.343644308310068 24.121332327688521 -1.0846223776529416
		13.343644308310068 24.121332327688521 -1.0846223776529416
		11.343644308310068 24.121332327688521 -1.0846223776529416
		11.343644308310068 24.121332327688521 0.91537762234705833
		11.343644308310068 26.121332327688521 0.91537762234705833
		11.343644308310068 24.121332327688521 0.91537762234705833
		13.343644308310068 24.121332327688521 0.91537762234705833
		;
createNode parentConstraint -n "lt_arm_icon_parentConstraint1" -p "lt_arm_icon";
	rename -uid "22600F81-CA4A-A671-74AB-8BB0410C1C7F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "lt_arm_01_fk_icon" -p "icon_grp";
	rename -uid "43320170-894E-EE12-7C4C-DE8665578B03";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 5.5743023094650761 5.5743023094650761 5.5743023094650761 ;
	setAttr ".rp" -type "double3" 8.5700054168701154 79.696846008300824 -1.7711960077285778 ;
	setAttr ".sp" -type "double3" 8.5700054168701154 79.696846008300824 -1.7711960077285778 ;
createNode nurbsCurve -n "lt_arm_01_fk_iconShape" -p "lt_arm_01_fk_icon";
	rename -uid "6CC4E226-1B42-EC9C-523F-62AEBB8B7A2C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "lt_gimbal_icon" -p "lt_arm_01_fk_icon";
	rename -uid "A1A8F259-3545-1AD6-ACCE-3B9FC09FB18F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".t" -type "double3" 1.6838006264603997 15.658519768439589 -0.34799755686580758 ;
	setAttr ".s" -type "double3" 0.80352397174150814 0.80352397174150814 0.80352397174150814 ;
	setAttr ".rp" -type "double3" 6.8862047904097148 64.038326239861235 -1.42319845086277 ;
	setAttr ".sp" -type "double3" 8.5700054168701154 79.696846008300824 -1.7711960077285778 ;
	setAttr ".spt" -type "double3" -1.6838006264604006 -15.658519768439584 0.34799755686580791 ;
createNode nurbsCurve -n "lt_gimbal_iconShape" -p "lt_gimbal_icon";
	rename -uid "37561186-EE4D-CCAE-9F29-A6984531F8C6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		8.6784004761347884 78.913250224887037 -0.99510160839788808
		8.5630329520563802 78.588674223978259 -1.7701769419440754
		8.4517498033026879 78.913250224886454 -2.5458492304058726
		8.409739189150045 79.696846008300412 -2.8677401671593357
		8.4616103576054442 80.480441791714625 -2.5472904070592666
		8.5769778816838524 80.805017792623403 -1.7722150735130799
		8.6882610304375447 80.480441791715208 -0.99654278505128246
		8.7302716445901876 79.69684600830125 -0.67465184829781899
		8.6784004761347884 78.913250224887037 -0.99510160839788808
		8.5630329520563802 78.588674223978259 -1.7701769419440754
		8.4517498033026879 78.913250224886454 -2.5458492304058726
		;
createNode parentConstraint -n "lt_arm_01_fk_icon_parentConstraint1" -p "lt_arm_01_fk_icon";
	rename -uid "65B041A1-FF47-6F83-7765-14B00C97E67B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 1.7763568394002505e-15 -4.2632564145606011e-14 1.1102230246251565e-15 ;
	setAttr -k on ".w0";
createNode transform -n "lt_arm_02_fk_icon" -p "icon_grp";
	rename -uid "91C079F8-3646-2BCA-03EE-FCBC6818D258";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 4.5835258967668882 4.5835258967668882 4.5835258967668882 ;
	setAttr ".rp" -type "double3" 25.346616744995128 79.589035034179659 -4.2231941223144656 ;
	setAttr ".sp" -type "double3" 25.346616744995128 79.589035034179659 -4.2231941223144656 ;
createNode nurbsCurve -n "lt_arm_02_fk_iconShape" -p "lt_arm_02_fk_icon";
	rename -uid "05D20A64-1E46-6892-C6E7-FB864018C5AB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		25.121030016685886 78.805467732073055 -3.4727094333237787
		25.335293631058356 78.480903528508392 -4.2264668213274605
		25.556190172006684 78.805467732073026 -4.9783071066348938
		25.654321441724655 79.589035034179645 -5.2878124468514436
		25.572203473304366 80.372602336286249 -4.9736788113051515
		25.3579398589319 80.697166539850926 -4.2199214233014706
		25.137043317983572 80.372602336286278 -3.4680811379940382
		25.038912048265601 79.589035034179688 -3.1585757977774893
		25.121030016685886 78.805467732073055 -3.4727094333237787
		25.335293631058356 78.480903528508392 -4.2264668213274605
		25.556190172006684 78.805467732073026 -4.9783071066348938
		;
createNode parentConstraint -n "lt_arm_02_fk_icon_parentConstraint1" -p "lt_arm_02_fk_icon";
	rename -uid "A8AF6344-0949-80E3-6CE0-8BA264AA5B5D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" -1.0658141036401503e-14 2.8421709430404007e-14 1.2434497875801753e-14 ;
	setAttr -k on ".w0";
createNode transform -n "lt_hand_icon" -p "icon_grp";
	rename -uid "6D3D54BF-604B-60FC-42B8-7DA88969A401";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 4.2271522085401374 4.2271522085401374 4.2271522085401374 ;
createNode nurbsCurve -n "lt_hand_iconShape" -p "lt_hand_icon";
	rename -uid "0CC2C763-EF4C-1628-280C-AB825802740C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "lt_hand_icon_parentConstraint1" -p "lt_hand_icon";
	rename -uid "FD1B857B-3C40-7A24-6819-FBAEEA3CE61F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_hand_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.6818590772530868 2.397389295189555 0.87459895453736092 ;
	setAttr ".rst" -type "double3" 47.853573859967931 82.462811353295024 0.60701001129433418 ;
	setAttr -k on ".w0";
createNode transform -n "lt_thumb_01_fk_pivot_icon" -p "icon_grp";
	rename -uid "C213F49E-A74A-2E45-FBA3-6F8226F2CFA6";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 43.128185272216768 79.977188110351548 2.7199199199676656 ;
	setAttr ".sp" -type "double3" 43.128185272216768 79.977188110351548 2.7199199199676656 ;
createNode nurbsCurve -n "lt_thumb_01_fk_pivot_iconShape" -p "lt_thumb_01_fk_pivot_icon";
	rename -uid "BE2F51CA-D641-2C58-A78B-43ADA9008552";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "lt_thumb_01_fk_pivot_icon_parentConstraint1" -p "lt_thumb_01_fk_pivot_icon";
	rename -uid "5127FB9A-9A43-8A3A-F83E-408E2761A6FA";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_thumb_01_pivot_locW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.4210854715202004e-14 0 1.4210854715202004e-14 ;
	setAttr ".rst" -type "double3" 1.4210854715202004e-14 1.4210854715202004e-14 4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_thumb_02_fk_icon" -p "icon_grp";
	rename -uid "7579A69B-FF46-6819-0B7E-E7822B39238F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 41.796833038330092 79.977188110351577 3.2891368865966939 ;
	setAttr ".sp" -type "double3" 41.796833038330092 79.977188110351577 3.2891368865966939 ;
createNode nurbsCurve -n "lt_thumb_02_fk_iconShape" -p "lt_thumb_02_fk_icon";
	rename -uid "116E30DF-8E45-4564-AFAE-139427D209E3";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "lt_thumb_02_fk_icon_parentConstraint1" -p "lt_thumb_02_fk_icon";
	rename -uid "68EC44EC-234C-845A-8FFD-7BA6FB0BCBB4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_thumb_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.1054273576010019e-15 0 1.3322676295501878e-14 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 -1.4210854715202004e-14 -4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_thumb_03_fk_icon" -p "icon_grp";
	rename -uid "C51836FE-0547-4BA6-1428-BFA3AFB31F98";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 42.376647949218764 79.273635864257827 4.1936120986938406 ;
	setAttr ".sp" -type "double3" 42.376647949218764 79.273635864257827 4.1936120986938406 ;
createNode nurbsCurve -n "lt_thumb_03_fk_iconShape" -p "lt_thumb_03_fk_icon";
	rename -uid "8B39C4A8-3B4D-8876-228B-75AD8470C527";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		42.992719416848459 79.554065247615455 5.0710570628093024
		42.698331629699567 80.230036802135572 4.6517727834630733
		42.21550590531912 80.345761658313251 3.9641041887251696
		41.827075004786565 79.833449764903293 3.410878214975007
		41.760576481589084 78.993206480900199 3.3161671345783681
		42.054964268737976 78.317234926380067 3.7354514139246007
		42.537789993118423 78.201510070202403 4.4231200086625009
		42.926220893650964 78.713821963612361 4.976345982412667
		42.992719416848459 79.554065247615455 5.0710570628093024
		42.698331629699567 80.230036802135572 4.6517727834630733
		42.21550590531912 80.345761658313251 3.9641041887251696
		;
createNode parentConstraint -n "lt_thumb_03_fk_icon_parentConstraint1" -p "lt_thumb_03_fk_icon";
	rename -uid "78592508-EE41-F0CB-BCCC-09A5D7013918";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_thumb_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.1054273576010019e-15 1.4210854715202004e-14 
		-7.1054273576010019e-15 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_thumb_04_fk_icon" -p "icon_grp";
	rename -uid "11426E8D-7F48-D348-9228-699136845BB8";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 43.381378173828182 78.25018310546875 5.6246075630187846 ;
	setAttr ".sp" -type "double3" 43.381378173828182 78.25018310546875 5.6246075630187846 ;
createNode nurbsCurve -n "lt_thumb_04_fk_iconShape" -p "lt_thumb_04_fk_icon";
	rename -uid "306BC549-594D-7948-1345-99B82BFE8DFF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		44.016860769836427 78.567103957066251 6.4753821520390709
		43.696625287677328 79.225164644040092 6.0466556811097654
		43.19172232172437 79.312094368782226 5.370699146576797
		42.7979171817504 78.776970877512056 4.8434787187948736
		42.745895577819923 77.933262253871234 4.7738329739984842
		43.066131059979021 77.275201566897394 5.2025594449277897
		43.571034025931979 77.18827184215526 5.878515979460758
		43.964839165905957 77.723395333425415 6.4057364072426886
		44.016860769836427 78.567103957066251 6.4753821520390709
		43.696625287677328 79.225164644040092 6.0466556811097654
		43.19172232172437 79.312094368782226 5.370699146576797
		;
createNode parentConstraint -n "lt_thumb_04_fk_icon_parentConstraint1" -p "lt_thumb_04_fk_icon";
	rename -uid "F8CD6DB1-C14F-308A-59BE-00AF21A781AB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_thumb_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 5.6843418860808015e-14 1.4210854715202004e-14 
		-1.4210854715202004e-14 ;
	setAttr ".rst" -type "double3" 0 1.4210854715202004e-14 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_index_01_fk_icon" -p "icon_grp";
	rename -uid "BCB13FB0-2242-2CD7-A0A8-CF97A97E158C";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 44.905929565429688 79.977188110351562 2.7693607807159424 ;
	setAttr ".sp" -type "double3" 44.905929565429688 79.977188110351562 2.7693607807159424 ;
createNode nurbsCurve -n "lt_index_01_fk_iconShape" -p "lt_index_01_fk_icon";
	rename -uid "DEE7FD40-6B46-94CB-6CED-CABBB2F66207";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		45.689541190320909 79.193576485460341 2.7693607807159424
		44.905929565429688 78.868993922797173 2.7693607807159424
		44.122317940538466 79.193576485460341 2.7693607807159424
		43.797735377875298 79.977188110351562 2.7693607807159424
		44.122317940538466 80.760799735242784 2.7693607807159424
		44.905929565429688 81.085382297905952 2.7693607807159424
		45.689541190320909 80.760799735242784 2.7693607807159424
		46.014123752984077 79.977188110351562 2.7693607807159424
		45.689541190320909 79.193576485460341 2.7693607807159424
		44.905929565429688 78.868993922797173 2.7693607807159424
		44.122317940538466 79.193576485460341 2.7693607807159424
		;
createNode parentConstraint -n "lt_index_01_fk_icon_parentConstraint1" -p "lt_index_01_fk_icon";
	rename -uid "291FCD80-7E43-89DD-A8D3-8E8C895D5107";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_index_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 1.4210854715202004e-14 0 ;
	setAttr ".rst" -type "double3" 0 1.4210854715202004e-14 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_index_02_fk_icon" -p "icon_grp";
	rename -uid "C2E68AED-134F-A9CB-6E33-E68DAD4C4C0D";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 47.264728546142592 79.977188110351562 2.7693607807159433 ;
	setAttr ".sp" -type "double3" 47.264728546142592 79.977188110351562 2.7693607807159433 ;
createNode nurbsCurve -n "lt_index_02_fk_iconShape" -p "lt_index_02_fk_icon";
	rename -uid "12004B0D-8E48-056F-4921-3D83847377BF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		48.048340171033814 79.193576485460341 2.7693607807159433
		47.264728546142592 78.868993922797173 2.7693607807159433
		46.48111692125137 79.193576485460341 2.7693607807159433
		46.156534358588203 79.977188110351562 2.7693607807159433
		46.48111692125137 80.760799735242784 2.7693607807159433
		47.264728546142592 81.085382297905952 2.7693607807159433
		48.048340171033814 80.760799735242784 2.7693607807159433
		48.372922733696981 79.977188110351562 2.7693607807159433
		48.048340171033814 79.193576485460341 2.7693607807159433
		47.264728546142592 78.868993922797173 2.7693607807159433
		46.48111692125137 79.193576485460341 2.7693607807159433
		;
createNode parentConstraint -n "lt_index_02_fk_icon_parentConstraint1" -p "lt_index_02_fk_icon";
	rename -uid "4939EC13-5741-3D79-AE2C-7E85D38EE124";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_index_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.4210854715202004e-14 -1.4210854715202004e-14 
		4.4408920985006262e-16 ;
	setAttr ".rst" -type "double3" 0 -1.4210854715202004e-14 -4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_index_03_fk_icon" -p "icon_grp";
	rename -uid "9B537B9B-4F40-A340-C108-C6BA1AC5F72D";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 48.914730072021506 79.977188110351548 2.7693607807159433 ;
	setAttr ".sp" -type "double3" 48.914730072021506 79.977188110351548 2.7693607807159433 ;
createNode nurbsCurve -n "lt_index_03_fk_iconShape" -p "lt_index_03_fk_icon";
	rename -uid "749D1D63-F44C-3B17-9BA4-B4BE7C5BC033";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		49.698341696912728 79.193576485460326 2.7693607807159433
		48.914730072021506 78.868993922797159 2.7693607807159433
		48.131118447130284 79.193576485460326 2.7693607807159433
		47.806535884467117 79.977188110351548 2.7693607807159433
		48.131118447130284 80.76079973524277 2.7693607807159433
		48.914730072021506 81.085382297905937 2.7693607807159433
		49.698341696912728 80.76079973524277 2.7693607807159433
		50.022924259575895 79.977188110351548 2.7693607807159433
		49.698341696912728 79.193576485460326 2.7693607807159433
		48.914730072021506 78.868993922797159 2.7693607807159433
		48.131118447130284 79.193576485460326 2.7693607807159433
		;
createNode parentConstraint -n "lt_index_03_fk_icon_parentConstraint1" -p "lt_index_03_fk_icon";
	rename -uid "941DC147-CB4F-B780-9568-27B0CCA8A76A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_index_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 2.1316282072803006e-14 -1.4210854715202004e-14 
		8.8817841970012523e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_index_04_fk_icon" -p "icon_grp";
	rename -uid "EAC08595-6040-AF83-3941-B48E56FBFED0";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 50.564731597900384 79.977188110351562 2.7693607807159442 ;
	setAttr ".sp" -type "double3" 50.564731597900384 79.977188110351562 2.7693607807159442 ;
createNode nurbsCurve -n "lt_index_04_fk_iconShape" -p "lt_index_04_fk_icon";
	rename -uid "D463BD2A-D844-3544-0AF9-7E98117A4709";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		51.348343222791605 79.193576485460341 2.7693607807159442
		50.564731597900384 78.868993922797173 2.7693607807159442
		49.781119973009162 79.193576485460341 2.7693607807159442
		49.456537410345994 79.977188110351562 2.7693607807159442
		49.781119973009162 80.760799735242784 2.7693607807159442
		50.564731597900384 81.085382297905952 2.7693607807159442
		51.348343222791605 80.760799735242784 2.7693607807159442
		51.672925785454773 79.977188110351562 2.7693607807159442
		51.348343222791605 79.193576485460341 2.7693607807159442
		50.564731597900384 78.868993922797173 2.7693607807159442
		49.781119973009162 79.193576485460341 2.7693607807159442
		;
createNode parentConstraint -n "lt_index_04_fk_icon_parentConstraint1" -p "lt_index_04_fk_icon";
	rename -uid "263642D4-5A4D-010F-1BA7-369135D66680";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_index_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 0 2.2204460492503131e-15 ;
	setAttr ".rst" -type "double3" 0 0 4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_middle_01_fk_icon" -p "icon_grp";
	rename -uid "AD19CD01-9B40-0A55-F6F6-14B89B3C8A3C";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 45.393089294433594 79.977188110351562 0.89764130115509033 ;
	setAttr ".sp" -type "double3" 45.393089294433594 79.977188110351562 0.89764130115509033 ;
createNode nurbsCurve -n "lt_middle_01_fk_iconShape" -p "lt_middle_01_fk_icon";
	rename -uid "ABEA553C-BA4D-FFEE-514C-C691856A9B12";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		46.176700919324816 79.193576485460341 0.89764130115509044
		45.393089294433594 78.868993922797173 0.89764130115509044
		44.609477669542372 79.193576485460341 0.89764130115509044
		44.284895106879205 79.977188110351562 0.89764130115509033
		44.609477669542372 80.760799735242784 0.89764130115509022
		45.393089294433594 81.085382297905952 0.89764130115509022
		46.176700919324816 80.760799735242784 0.89764130115509022
		46.501283481987983 79.977188110351562 0.89764130115509033
		46.176700919324816 79.193576485460341 0.89764130115509044
		45.393089294433594 78.868993922797173 0.89764130115509044
		44.609477669542372 79.193576485460341 0.89764130115509044
		;
createNode parentConstraint -n "lt_middle_01_fk_icon_parentConstraint1" -p "lt_middle_01_fk_icon";
	rename -uid "7794A9C4-074D-1DD5-B8E8-14801429121E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_middle_01_locW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "lt_middle_02_fk_icon" -p "icon_grp";
	rename -uid "8F0D7A17-1B44-49A8-30E4-81ADC60A8388";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 47.732669830322259 79.977188110351562 0.89764130115509033 ;
	setAttr ".sp" -type "double3" 47.732669830322259 79.977188110351562 0.89764130115509033 ;
createNode nurbsCurve -n "lt_middle_02_fk_iconShape" -p "lt_middle_02_fk_icon";
	rename -uid "2517B1E1-9E4D-705C-B181-578E93B9C768";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		48.51628145521348 79.193576485460341 0.89764130115509044
		47.732669830322259 78.868993922797173 0.89764130115509044
		46.949058205431037 79.193576485460341 0.89764130115509044
		46.624475642767869 79.977188110351562 0.89764130115509033
		46.949058205431037 80.760799735242784 0.89764130115509022
		47.732669830322259 81.085382297905952 0.89764130115509022
		48.51628145521348 80.760799735242784 0.89764130115509022
		48.840864017876648 79.977188110351562 0.89764130115509033
		48.51628145521348 79.193576485460341 0.89764130115509044
		47.732669830322259 78.868993922797173 0.89764130115509044
		46.949058205431037 79.193576485460341 0.89764130115509044
		;
createNode parentConstraint -n "lt_middle_02_fk_icon_parentConstraint1" -p "lt_middle_02_fk_icon";
	rename -uid "C56470FB-5B46-27C9-090D-C8AA639D1708";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_middle_02_locW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 1.4210854715202004e-14 
		0 ;
	setAttr ".rst" -type "double3" 0 1.4210854715202004e-14 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_middle_03_fk_icon" -p "icon_grp";
	rename -uid "07698FEB-EE48-EB09-7205-84854A5E0332";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 49.369224548339851 79.977188110351577 0.89764130115509044 ;
	setAttr ".sp" -type "double3" 49.369224548339851 79.977188110351577 0.89764130115509044 ;
createNode nurbsCurve -n "lt_middle_03_fk_iconShape" -p "lt_middle_03_fk_icon";
	rename -uid "6D4FA1D8-4542-0001-A534-9FBAC26E7768";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		50.152836173231073 79.193576485460355 0.89764130115509055
		49.369224548339851 78.868993922797188 0.89764130115509055
		48.585612923448629 79.193576485460355 0.89764130115509055
		48.261030360785462 79.977188110351577 0.89764130115509044
		48.585612923448629 80.760799735242799 0.89764130115509033
		49.369224548339851 81.085382297905966 0.89764130115509033
		50.152836173231073 80.760799735242799 0.89764130115509033
		50.47741873589424 79.977188110351577 0.89764130115509044
		50.152836173231073 79.193576485460355 0.89764130115509055
		49.369224548339851 78.868993922797188 0.89764130115509055
		48.585612923448629 79.193576485460355 0.89764130115509055
		;
createNode parentConstraint -n "lt_middle_03_fk_icon_parentConstraint1" -p "lt_middle_03_fk_icon";
	rename -uid "0F3D0A53-344C-AD70-E7D8-FA91006B4CAD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_middle_03_locW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.1054273576010019e-15 1.4210854715202004e-14 
		0 ;
	setAttr ".rst" -type "double3" 0 0 -1.1102230246251565e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_middle_04_fk_icon" -p "icon_grp";
	rename -uid "A4EDDC1C-FF41-326A-47B3-BAA24841A719";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 51.005779266357429 79.977188110351562 0.89764130115509044 ;
	setAttr ".sp" -type "double3" 51.005779266357429 79.977188110351562 0.89764130115509044 ;
createNode nurbsCurve -n "lt_middle_04_fk_iconShape" -p "lt_middle_04_fk_icon";
	rename -uid "31065CEF-9C49-496F-289A-A3A1B50DF6A7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		51.789390891248651 79.193576485460341 0.89764130115509055
		51.005779266357429 78.868993922797173 0.89764130115509055
		50.222167641466207 79.193576485460341 0.89764130115509055
		49.89758507880304 79.977188110351562 0.89764130115509044
		50.222167641466207 80.760799735242784 0.89764130115509033
		51.005779266357429 81.085382297905952 0.89764130115509033
		51.789390891248651 80.760799735242784 0.89764130115509033
		52.113973453911818 79.977188110351562 0.89764130115509044
		51.789390891248651 79.193576485460341 0.89764130115509055
		51.005779266357429 78.868993922797173 0.89764130115509055
		50.222167641466207 79.193576485460341 0.89764130115509055
		;
createNode parentConstraint -n "lt_middle_04_fk_icon_parentConstraint1" -p "lt_middle_04_fk_icon";
	rename -uid "E3484299-7E45-6213-046B-79AA104ED363";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_middle_04_locW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 1.1102230246251565e-16 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_ring_01_fk_icon" -p "icon_grp";
	rename -uid "E7DA826B-7448-B7C3-C5C4-BAB66870D7E0";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 45.008491516113281 79.977188110351562 -0.99971818923950195 ;
	setAttr ".sp" -type "double3" 45.008491516113281 79.977188110351562 -0.99971818923950195 ;
createNode nurbsCurve -n "lt_ring_01_fk_iconShape" -p "lt_ring_01_fk_icon";
	rename -uid "8EFE4597-F143-9F1D-76CA-70B15B238758";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		45.792103141004503 79.193576485460341 -0.99971818923950184
		45.008491516113281 78.868993922797173 -0.99971818923950184
		44.224879891222059 79.193576485460341 -0.99971818923950184
		43.900297328558892 79.977188110351562 -0.99971818923950195
		44.224879891222059 80.760799735242784 -0.99971818923950206
		45.008491516113281 81.085382297905952 -0.99971818923950206
		45.792103141004503 80.760799735242784 -0.99971818923950206
		46.11668570366767 79.977188110351562 -0.99971818923950195
		45.792103141004503 79.193576485460341 -0.99971818923950184
		45.008491516113281 78.868993922797173 -0.99971818923950184
		44.224879891222059 79.193576485460341 -0.99971818923950184
		;
createNode parentConstraint -n "lt_ring_01_fk_icon_parentConstraint1" -p "lt_ring_01_fk_icon";
	rename -uid "D170B8BE-4542-ABD3-EA62-66ABF9D09CD4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_ring_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 0 1.1102230246251565e-16 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 0 1.1102230246251565e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_ring_02_fk_icon" -p "icon_grp";
	rename -uid "436E6DB5-254E-6BDA-9028-608A1F3AE826";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 47.170722961425781 79.977188110351562 -0.99971818923950184 ;
	setAttr ".sp" -type "double3" 47.170722961425781 79.977188110351562 -0.99971818923950184 ;
createNode nurbsCurve -n "lt_ring_02_fk_iconShape" -p "lt_ring_02_fk_icon";
	rename -uid "14644282-AF45-1E9A-16F6-C3B2B5C7F975";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		47.954334586317003 79.193576485460341 -0.99971818923950173
		47.170722961425781 78.868993922797173 -0.99971818923950173
		46.387111336534559 79.193576485460341 -0.99971818923950173
		46.062528773871392 79.977188110351562 -0.99971818923950184
		46.387111336534559 80.760799735242784 -0.99971818923950195
		47.170722961425781 81.085382297905952 -0.99971818923950195
		47.954334586317003 80.760799735242784 -0.99971818923950195
		48.27891714898017 79.977188110351562 -0.99971818923950184
		47.954334586317003 79.193576485460341 -0.99971818923950173
		47.170722961425781 78.868993922797173 -0.99971818923950173
		46.387111336534559 79.193576485460341 -0.99971818923950173
		;
createNode parentConstraint -n "lt_ring_02_fk_icon_parentConstraint1" -p "lt_ring_02_fk_icon";
	rename -uid "5E7DB55F-514F-ECC6-9603-B29389CF3F1F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_ring_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 0 -1.1102230246251565e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_ring_03_fk_icon" -p "icon_grp";
	rename -uid "9661FD81-D947-9529-06D5-84876BC84A9F";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 48.683223724365234 79.977188110351562 -0.99971818923950206 ;
	setAttr ".sp" -type "double3" 48.683223724365234 79.977188110351562 -0.99971818923950206 ;
createNode nurbsCurve -n "lt_ring_03_fk_iconShape" -p "lt_ring_03_fk_icon";
	rename -uid "7326E473-9E41-3967-6050-03957CE028C8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		49.466835349256456 79.193576485460341 -0.99971818923950195
		48.683223724365234 78.868993922797173 -0.99971818923950195
		47.899612099474012 79.193576485460341 -0.99971818923950195
		47.575029536810845 79.977188110351562 -0.99971818923950206
		47.899612099474012 80.760799735242784 -0.99971818923950218
		48.683223724365234 81.085382297905952 -0.99971818923950218
		49.466835349256456 80.760799735242784 -0.99971818923950218
		49.791417911919623 79.977188110351562 -0.99971818923950206
		49.466835349256456 79.193576485460341 -0.99971818923950195
		48.683223724365234 78.868993922797173 -0.99971818923950195
		47.899612099474012 79.193576485460341 -0.99971818923950195
		;
createNode parentConstraint -n "lt_ring_03_fk_icon_parentConstraint1" -p "lt_ring_03_fk_icon";
	rename -uid "D4789204-2247-EE5B-02A7-1FB34B49273A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_ring_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 1.4210854715202004e-14 
		-2.2204460492503131e-16 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 1.4210854715202004e-14 -1.1102230246251565e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_ring_04_fk_icon" -p "icon_grp";
	rename -uid "BAB11A13-3A4F-F187-1084-86820A26FEAF";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 50.19572448730468 79.977188110351577 -0.99971818923950195 ;
	setAttr ".sp" -type "double3" 50.19572448730468 79.977188110351577 -0.99971818923950195 ;
createNode nurbsCurve -n "lt_ring_04_fk_iconShape" -p "lt_ring_04_fk_icon";
	rename -uid "46D80B04-A34A-9D2E-45F7-D9B7D953E1AB";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		50.979336112195902 79.193576485460355 -0.99971818923950184
		50.19572448730468 78.868993922797188 -0.99971818923950184
		49.412112862413458 79.193576485460355 -0.99971818923950184
		49.087530299750291 79.977188110351577 -0.99971818923950195
		49.412112862413458 80.760799735242799 -0.99971818923950206
		50.19572448730468 81.085382297905966 -0.99971818923950206
		50.979336112195902 80.760799735242799 -0.99971818923950206
		51.303918674859069 79.977188110351577 -0.99971818923950195
		50.979336112195902 79.193576485460355 -0.99971818923950184
		50.19572448730468 78.868993922797188 -0.99971818923950184
		49.412112862413458 79.193576485460355 -0.99971818923950184
		;
createNode parentConstraint -n "lt_ring_04_fk_icon_parentConstraint1" -p "lt_ring_04_fk_icon";
	rename -uid "7CCA8741-F14E-4FAA-7EA7-07B484835080";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_ring_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 1.4210854715202004e-14 
		-1.1102230246251565e-16 ;
	setAttr ".rst" -type "double3" 0 0 -1.1102230246251565e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_pinky_01_fk_icon" -p "icon_grp";
	rename -uid "20CD0FCF-E44F-B2C6-DC76-C5B0E3F43B30";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 44.521331787109375 79.977188110351562 -2.6663174629211426 ;
	setAttr ".sp" -type "double3" 44.521331787109375 79.977188110351562 -2.6663174629211426 ;
createNode nurbsCurve -n "lt_pinky_01_fk_iconShape" -p "lt_pinky_01_fk_icon";
	rename -uid "DFF9874B-6C48-F077-5E7B-81BC8FE0060A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		45.304943412000597 79.193576485460341 -2.6663174629211426
		44.521331787109375 78.868993922797173 -2.6663174629211426
		43.737720162218153 79.193576485460341 -2.6663174629211426
		43.413137599554986 79.977188110351562 -2.6663174629211426
		43.737720162218153 80.760799735242784 -2.6663174629211426
		44.521331787109375 81.085382297905952 -2.6663174629211426
		45.304943412000597 80.760799735242784 -2.6663174629211426
		45.629525974663764 79.977188110351562 -2.6663174629211426
		45.304943412000597 79.193576485460341 -2.6663174629211426
		44.521331787109375 78.868993922797173 -2.6663174629211426
		43.737720162218153 79.193576485460341 -2.6663174629211426
		;
createNode parentConstraint -n "lt_pinky_01_fk_icon_parentConstraint1" -p "lt_pinky_01_fk_icon";
	rename -uid "2EDD9EF9-3340-1C85-4A9E-09AA1DB7FD65";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_pinky_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 0 4.4408920985006262e-16 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 0 4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_pinky_02_fk_icon" -p "icon_grp";
	rename -uid "DA896F6F-B148-6A54-80DA-29B4104F1584";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 46.455326080322259 79.977188110351562 -2.6663174629211421 ;
	setAttr ".sp" -type "double3" 46.455326080322259 79.977188110351562 -2.6663174629211421 ;
createNode nurbsCurve -n "lt_pinky_02_fk_iconShape" -p "lt_pinky_02_fk_icon";
	rename -uid "FDA5DB03-DA42-0282-2EF2-28AC6BF4E533";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		47.23893770521348 79.193576485460341 -2.6663174629211421
		46.455326080322259 78.868993922797173 -2.6663174629211421
		45.671714455431037 79.193576485460341 -2.6663174629211421
		45.347131892767869 79.977188110351562 -2.6663174629211421
		45.671714455431037 80.760799735242784 -2.6663174629211421
		46.455326080322259 81.085382297905952 -2.6663174629211421
		47.23893770521348 80.760799735242784 -2.6663174629211421
		47.563520267876648 79.977188110351562 -2.6663174629211421
		47.23893770521348 79.193576485460341 -2.6663174629211421
		46.455326080322259 78.868993922797173 -2.6663174629211421
		45.671714455431037 79.193576485460341 -2.6663174629211421
		;
createNode parentConstraint -n "lt_pinky_02_fk_icon_parentConstraint1" -p "lt_pinky_02_fk_icon";
	rename -uid "4BCFD267-6B43-B51A-5ACC-68B8723A4667";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_pinky_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -7.1054273576010019e-15 1.4210854715202004e-14 
		4.4408920985006262e-16 ;
	setAttr ".rst" -type "double3" 0 1.4210854715202004e-14 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_pinky_03_fk_icon" -p "icon_grp";
	rename -uid "F24B5EFB-2E45-318A-8342-F797AB02E423";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 47.808174133300781 79.977188110351577 -2.6663174629211426 ;
	setAttr ".sp" -type "double3" 47.808174133300781 79.977188110351577 -2.6663174629211426 ;
createNode nurbsCurve -n "lt_pinky_03_fk_iconShape" -p "lt_pinky_03_fk_icon";
	rename -uid "AA9FD2B6-6C48-463C-8540-968A60CDBCA8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		48.591785758192003 79.193576485460355 -2.6663174629211426
		47.808174133300781 78.868993922797188 -2.6663174629211426
		47.024562508409559 79.193576485460355 -2.6663174629211426
		46.699979945746392 79.977188110351577 -2.6663174629211426
		47.024562508409559 80.760799735242799 -2.6663174629211426
		47.808174133300781 81.085382297905966 -2.6663174629211426
		48.591785758192003 80.760799735242799 -2.6663174629211426
		48.91636832085517 79.977188110351577 -2.6663174629211426
		48.591785758192003 79.193576485460355 -2.6663174629211426
		47.808174133300781 78.868993922797188 -2.6663174629211426
		47.024562508409559 79.193576485460355 -2.6663174629211426
		;
createNode parentConstraint -n "lt_pinky_03_fk_icon_parentConstraint1" -p "lt_pinky_03_fk_icon";
	rename -uid "20E89668-A245-340F-8844-16BF0DF33E07";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_pinky_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 1.4210854715202004e-14 4.4408920985006262e-16 ;
	setAttr ".rst" -type "double3" 0 0 4.4408920985006262e-16 ;
	setAttr -k on ".w0";
createNode transform -n "lt_pinky_04_fk_icon" -p "icon_grp";
	rename -uid "D2866688-834C-49A6-2D06-05BDDA90B814";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".rp" -type "double3" 49.16102218627929 79.977188110351562 -2.6663174629211426 ;
	setAttr ".sp" -type "double3" 49.16102218627929 79.977188110351562 -2.6663174629211426 ;
createNode nurbsCurve -n "lt_pinky_04_fk_iconShape" -p "lt_pinky_04_fk_icon";
	rename -uid "4D91B7AB-6540-ED34-AF23-C590D838EE8D";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		49.944633811170512 79.193576485460341 -2.6663174629211426
		49.16102218627929 78.868993922797173 -2.6663174629211426
		48.377410561388068 79.193576485460341 -2.6663174629211426
		48.052827998724901 79.977188110351562 -2.6663174629211426
		48.377410561388068 80.760799735242784 -2.6663174629211426
		49.16102218627929 81.085382297905952 -2.6663174629211426
		49.944633811170512 80.760799735242784 -2.6663174629211426
		50.269216373833679 79.977188110351562 -2.6663174629211426
		49.944633811170512 79.193576485460341 -2.6663174629211426
		49.16102218627929 78.868993922797173 -2.6663174629211426
		48.377410561388068 79.193576485460341 -2.6663174629211426
		;
createNode parentConstraint -n "lt_pinky_04_fk_icon_parentConstraint1" -p "lt_pinky_04_fk_icon";
	rename -uid "6430BF11-7F45-1AF5-DA1F-8A9FDB3E9C61";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_pinky_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.4210854715202004e-14 0 0 ;
	setAttr ".rst" -type "double3" -7.1054273576010019e-15 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "ct_neck_fk_icon" -p "icon_grp";
	rename -uid "7973B998-F042-015D-7E12-4096F3FED898";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".s" -type "double3" 5.2187142290595121 5.2187142290595121 5.2187142290595121 ;
	setAttr ".rp" -type "double3" 7.0461854497535625e-15 84.008064270019503 -1.4320060014724731 ;
	setAttr ".sp" -type "double3" 1.3501765263401646e-15 16.097463969618239 -0.27439824037472565 ;
	setAttr ".spt" -type "double3" 5.6960089234133974e-15 67.910600300401285 -1.1576077610977475 ;
createNode nurbsCurve -n "ct_neck_fk_iconShape" -p "ct_neck_fk_icon";
	rename -uid "A0D98752-804D-DF6E-338C-C0A9C4A693CE";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "ct_neck_fk_icon_parentConstraint1" -p "ct_neck_fk_icon";
	rename -uid "E5E68C46-7A44-812D-116F-B6B0734D0216";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_neck_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -1.5777218104420236e-30 0 0 ;
	setAttr ".rst" -type "double3" -1.5777218104420236e-30 1.4210854715202004e-14 0 ;
	setAttr -k on ".w0";
createNode transform -n "ct_neck_icon" -p "icon_grp";
	rename -uid "4C9BAF7C-E048-9F4D-0BCD-0D9730310A08";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".s" -type "double3" 3.5761550279758434 3.5761550279758434 3.5761550279758434 ;
	setAttr ".rp" -type "double3" 4.4953004128345597e-15 88.591758728027344 -0.39286234974861151 ;
	setAttr ".sp" -type "double3" 1.2570205647317719e-15 24.772907783634757 -0.10985607354135803 ;
	setAttr ".spt" -type "double3" 3.2382798481027878e-15 63.818850944392587 -0.28300627620725349 ;
createNode nurbsCurve -n "ct_neck_iconShape" -p "ct_neck_icon";
	rename -uid "A8A6C82D-D040-34C1-1ED4-5F9182D6C929";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122627 24.772907783634757 -0.89346769843258178
		1.1305888586534784e-15 24.772907783634757 -1.218050261095746
		-0.78361162489122305 24.772907783634757 -0.89346769843258222
		-1.1081941875543866 24.772907783634757 -0.10985607354135835
		-0.78361162489122327 24.772907783634757 0.67375555134986609
		9.2310002837271972e-16 24.772907783634757 0.99833811401303008
		0.78361162489122504 24.772907783634757 0.67375555134986631
		1.1081941875543893 24.772907783634757 -0.10985607354135743
		0.78361162489122627 24.772907783634757 -0.89346769843258178
		1.1305888586534784e-15 24.772907783634757 -1.218050261095746
		-0.78361162489122305 24.772907783634757 -0.89346769843258222
		;
createNode parentConstraint -n "ct_neck_icon_parentConstraint1" -p "ct_neck_icon";
	rename -uid "61E6C90A-CA4E-F9B1-FCA2-1DA2B8E6679D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_neck_04_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 7.8886090522101181e-31 1.4210854715202004e-14 
		-5.5511151231257827e-17 ;
	setAttr ".rst" -type "double3" 0 -1.4210854715202004e-14 -5.5511151231257827e-17 ;
	setAttr -k on ".w0";
createNode transform -n "lt_leg_ikfk_switch_icon" -p "icon_grp";
	rename -uid "AA27012C-9646-659F-EC21-718005C02167";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 3.5613859523694216 3.5613859523694216 3.5613859523694216 ;
	setAttr ".rp" -type "double3" 7.7717790603637695 5.2744808197021484 -1.2935034036636353 ;
	setAttr ".sp" -type "double3" 2.1822344346568605 1.4810191566552875 -0.36320225355049085 ;
	setAttr ".spt" -type "double3" 5.5895446257069086 3.7934616630468616 -0.93030115011314418 ;
createNode nurbsCurve -n "nurbsCircleShape1" -p "lt_leg_ikfk_switch_icon";
	rename -uid "74FF855F-D540-0DCD-802C-FEB45771E729";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "curveShape3" -p "lt_leg_ikfk_switch_icon";
	rename -uid "B63CF6CD-224C-C388-860C-7DB2A97180F7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		2.1822344346568601 1.4810191566552875 -4.1312022535504909
		2.1822344346568601 1.4810191566552875 -2.5952022535504904
		;
createNode nurbsCurve -n "curveShape4" -p "lt_leg_ikfk_switch_icon";
	rename -uid "111E68B4-F441-9DFE-25E9-7B934E4D938F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		2.1822344346568601 2.2490191566552875 -3.3632022535504906
		2.1822344346568605 0.71301915665528748 -3.3632022535504906
		;
createNode nurbsCurve -n "curveShape5" -p "lt_leg_ikfk_switch_icon";
	rename -uid "FCDB44E9-6D4A-E6B7-216E-A1AF46E626E8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		2.1822344346568601 1.4810191566552875 -2.3632022535504906
		2.1822344346568601 1.4810191566552875 -0.36320225355049057
		;
createNode parentConstraint -n "lt_leg_ikfk_switch_parentConstraint1" -p "lt_leg_ikfk_switch_icon";
	rename -uid "E179DADA-9943-A291-9949-6FBAB410D73A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -2.6645352591003757e-15 8.8817841970012523e-16 
		0 ;
	setAttr ".rst" -type "double3" -2.6645352591003757e-15 8.8817841970012523e-16 0 ;
	setAttr -k on ".w0";
createNode transform -n "lt_elbow_icon" -p "icon_grp";
	rename -uid "345A1C29-A944-D60C-DEEB-5AA6BAE87231";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "lt_elbow_iconShape" -p "lt_elbow_icon";
	rename -uid "2C748CCC-8543-6F0C-785F-D29398226ACC";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		1 1 -0.49139149999999532
		3 1 0.0078665000000057717
		3 2 0.0078665000000057717
		5 0 0.49139150000000598
		3 -2 0.0078665000000057717
		3 -1 0.0078665000000057717
		1 -1 -0.49139149999999532
		1 -3 0.0078665000000057717
		2 -3 0.0078665000000057717
		0 -5 0.49139150000000598
		-2 -3 0.0078665000000057717
		-1 -3 0.0078665000000057717
		-1 -1 -0.49139149999999532
		-3 -1 0.0078665000000057717
		-3 -2 0.0078665000000057717
		-5 0 0.49139150000000598
		-3 2 0.0078665000000057717
		-3 1 0.0078665000000057717
		-1 1 -0.49139149999999532
		-1 3 0.0078665000000057717
		-2 3 0.0078665000000057717
		0 5 0.49139150000000598
		2 3 0.0078665000000057717
		1 3 0.0078665000000057717
		1 1 -0.49139149999999532
		;
createNode transform -n "lt_arm_hybrid_icon" -p "lt_elbow_icon";
	rename -uid "F054477E-5F4E-FDB1-0A26-20A0682557EB";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 3.2674839585079725 3.2674839585079725 3.2674839585079725 ;
	setAttr ".rp" -type "double3" 1.4210854715202004e-14 9.2370555648813024e-14 1.517112124815867e-07 ;
	setAttr ".sp" -type "double3" 1.0872933804463948e-15 1.7396694087142317e-14 4.6430591368798158e-08 ;
	setAttr ".spt" -type "double3" 2.4654202983541065e-15 3.9446724773665704e-14 1.0528062111278855e-07 ;
createNode nurbsCurve -n "lt_arm_hybrid_iconShape" -p "lt_arm_hybrid_icon";
	rename -uid "46E77186-C24F-77B1-5989-D487F187DB05";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.22558672830924564 -0.7835673021066043 0.75048473542128491
		-0.011323113936774654 -1.1081315056712668 -0.003272652582396951
		0.20957342701155213 -0.78356730210663272 -0.75511293788983114
		0.30770469672952405 -1.4210854715202004e-14 -1.06461827810638
		0.22558672830923587 0.78356730210659009 -0.75048464256008796
		0.011323113936769325 1.1081315056712668 0.003272745443593017
		-0.20957342701155834 0.78356730210661851 0.75511303075102454
		-0.30770469672952938 2.8421709430404007e-14 1.0646183709675743
		-0.22558672830924564 -0.7835673021066043 0.75048473542128491
		-0.011323113936774654 -1.1081315056712668 -0.003272652582396951
		0.20957342701155213 -0.78356730210663272 -0.75511293788983114
		;
createNode pointConstraint -n "lt_arm_02_fk_icon_pointConstraint1" -p "lt_arm_hybrid_icon";
	rename -uid "9E6C58E4-FC4F-5BFF-7C65-BCB8A06FCA31";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".rp" -type "double3" -25.346616744995135 -79.589035034179645 4.2231941687450565 ;
	setAttr ".sp" -type "double3" -25.346616744995135 -79.589035034179645 4.2231941687450565 ;
	setAttr ".erp" yes;
	setAttr ".tg[0].tt" -type "double3" 16.776611328125 -0.10781097412109375 -2.4519981145858765 ;
	setAttr ".tg[0].tpm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 8.5700054168701172 79.696846008300781 -1.7711960077285767 1;
	setAttr ".cpim" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".crp" -type "double3" 25.346616744995128 79.589035034179659 -4.2231941223144656 ;
	setAttr ".o" -type "double3" 1.0658141036401503e-14 -2.8421709430404007e-14 -1.2434497875801753e-14 ;
createNode pointConstraint -n "lt_elbow_icon_pointConstraint1" -p "lt_elbow_icon";
	rename -uid "36A8920A-7C4C-7C38-3609-FD88333F5670";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0 0 -27.093582305031525 ;
	setAttr ".rst" -type "double3" 25.346616744995117 79.589035034179688 -31.316776427345978 ;
	setAttr -k on ".w0";
createNode transform -n "lt_knee_icon" -p "icon_grp";
	rename -uid "BD5C4CC5-7A49-DBF9-2BA9-14B6DA151ADC";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "lt_knee_iconShape" -p "lt_knee_icon";
	rename -uid "2320E0AA-4A4C-6706-BA47-B19353D69681";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		1 -1 0.49139149999999887
		3 -1 -0.0078665000000022189
		3 -2 -0.0078665000000022189
		5 0 -0.49139150000000242
		3 2 -0.0078664999999986662
		3 1 -0.0078664999999986662
		1 1 0.49139150000000242
		1 3 -0.0078664999999986662
		2 3 -0.0078664999999986662
		0 5 -0.49139149999999887
		-2 3 -0.0078664999999986662
		-1 3 -0.0078664999999986662
		-1 1 0.49139150000000242
		-3 1 -0.0078664999999986662
		-3 2 -0.0078664999999986662
		-5 0 -0.49139150000000242
		-3 -2 -0.0078665000000022189
		-3 -1 -0.0078665000000022189
		-1 -1 0.49139149999999887
		-1 -3 -0.0078665000000022189
		-2 -3 -0.0078665000000022189
		0 -5 -0.49139150000000242
		2 -3 -0.0078665000000022189
		1 -3 -0.0078665000000022189
		1 -1 0.49139149999999887
		;
createNode parentConstraint -n "lt_knee_icon_parentConstraint1" -p "lt_knee_icon";
	rename -uid "5099091C-2740-E09F-E56A-08A352B99BCD";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_leg_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -3.5527136788005009e-15 21.624165537651496 ;
	setAttr ".rst" -type "double3" 7.7717790603637695 23.924690246582028 23.289135697182136 ;
	setAttr -k on ".w0";
createNode transform -n "lt_arm_ikfk_switch_icon" -p "icon_grp";
	rename -uid "29082F4E-924A-8D2E-9680-5DB6E7F3573A";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 2.3470258676077136 2.3470258676077136 2.3470258676077136 ;
	setAttr ".rp" -type "double3" 39.032497406005859 79.437507629394588 -0.26758894324302696 ;
	setAttr ".sp" -type "double3" 16.630620882671 33.846029873698811 -0.11401192757870017 ;
	setAttr ".spt" -type "double3" 22.401876523334863 45.591477755695728 -0.15357701566432641 ;
createNode nurbsCurve -n "nurbsCircleShape1" -p "lt_arm_ikfk_switch_icon";
	rename -uid "C8116D64-C340-744A-3596-E5A2F9E0086A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		16.630620882670993 33.062418248807575 -3.897623552469923
		16.630620882670993 33.846029873698797 -4.2222061151330861
		16.630620882670993 34.629641498590026 -3.897623552469923
		16.630620882670993 34.954224061253186 -3.1140119275786997
		16.630620882670993 34.629641498590026 -2.3304003026874751
		16.630620882670993 33.846029873698797 -2.0058177400243111
		16.630620882670993 33.062418248807575 -2.3304003026874751
		16.630620882670993 32.737835686144408 -3.1140119275786988
		16.630620882670993 33.062418248807575 -3.897623552469923
		16.630620882670993 33.846029873698797 -4.2222061151330861
		16.630620882670993 34.629641498590026 -3.897623552469923
		;
createNode nurbsCurve -n "curveShape3" -p "lt_arm_ikfk_switch_icon";
	rename -uid "0354D429-AC42-327F-6FC0-5C97C3911808";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		16.630620882670993 33.846029873698797 -3.8820119275786991
		16.630620882670993 33.846029873698797 -2.346011927578699
		;
createNode nurbsCurve -n "curveShape4" -p "lt_arm_ikfk_switch_icon";
	rename -uid "734CF564-E944-64C7-FFC8-5B9731799C7F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		16.630620882670993 34.614029873698797 -3.1140119275786993
		16.630620882670993 33.078029873698796 -3.1140119275786993
		;
createNode nurbsCurve -n "curveShape5" -p "lt_arm_ikfk_switch_icon";
	rename -uid "22E43037-7A47-32E9-FFB8-CA96AD3C416C";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		16.630620882670993 33.846029873698797 -2.1140119275786993
		16.630620882670993 33.846029873698797 -0.11401192757869984
		;
createNode parentConstraint -n "lt_arm_ikfk_switch_parentConstraint1" -p "lt_arm_ikfk_switch_icon";
	rename -uid "CC50EB5C-A641-2CD3-30E5-88AF64B03F98";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_03_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 -5.6843418860808015e-14 2.2204460492503131e-16 ;
	setAttr -k on ".w0";
createNode transform -n "ct_moveAll" -p "icon_grp";
	rename -uid "5B4EEA91-604A-959A-2B6C-F7BCF1CE5F18";
	setAttr ".s" -type "double3" 26.677586104440266 26.677586104440266 26.677586104440266 ;
createNode nurbsCurve -n "moveAll_shape" -p "ct_moveAll";
	rename -uid "E91DC42A-7D4F-9F29-C08B-FC8ACD3EA188";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode nurbsCurve -n "xAxis_shape" -p "ct_moveAll";
	rename -uid "F5C7C7D2-9246-5FBF-10BA-37A3A639EA8C";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		1.108194208190024 0 -0.1593383279757766
		1.5540736561566149 0 -0.15933805993024167
		1.5540739222870454 0 -0.27040594385003053
		1.8202040869488232 0 0
		1.5540739222870454 0 0.27040594385003053
		1.5540736561566149 0 0.15933805993024167
		1.108194208190024 0 0.1593383279757766
		1.108194208190024 0 -0.1593383279757766
		;
createNode nurbsCurve -n "zAxis_shape" -p "ct_moveAll";
	rename -uid "A73D3F91-5545-82F1-1EEE-3785E0BB1E4F";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		0.15897464843442305 0 1.1081942074615634
		0.15897464843442305 0 1.5562579923699096
		0.26978921343059498 0 1.5562582598040975
		0 0 1.8236921803412289
		-0.26978921343059498 0 1.5562582598040975
		-0.15897464843442305 0 1.5562579923699096
		-0.15897464843442305 0 1.1081942074615634
		0.15897464843442305 0 1.1081942074615634
		;
createNode transform -n "ct_anim" -p "ct_moveAll";
	rename -uid "F2B7EA6E-4E46-6CC2-0BE5-94A8EE6D14FB";
	setAttr ".s" -type "double3" 0.8012877314036686 0.8012877314036686 0.8012877314036686 ;
createNode nurbsCurve -n "ct_animShape" -p "ct_anim";
	rename -uid "A98A8601-A44C-AE39-6E64-53AD78D925B2";
	setAttr -k off ".v";
	setAttr ".tw" yes;
	setAttr -s 11 ".cp[0:10]" -type "double3" -0.011429967272701291 0 0.03428990181810343 
		-0.011429967272701326 0 0.034289901818103319 -0.011429967272701291 0 0.03428990181810343 
		-0.011429967272701402 0 0.034289901818103416 -0.011429967272701291 0 0.03428990181810343 
		-0.011429967272701326 0 0.034289901818103319 -0.011429967272701291 0 0.03428990181810343 
		-0.011429967272701402 0 0.034289901818103423 0 0 0 0 0 0 0 0 0;
createNode transform -n "ct_head_icon" -p "icon_grp";
	rename -uid "C9BC5E5C-F844-F8CF-B70A-F0943C606413";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".rp" -type "double3" -1.9999999999999964 0 0 ;
	setAttr ".sp" -type "double3" -1.9999999999999964 0 0 ;
createNode nurbsCurve -n "ct_head_iconShape" -p "ct_head_icon";
	rename -uid "76FA03EA-6346-D5DD-5FED-09ACB818DE57";
	setAttr -k off ".v";
	setAttr ".tw" yes;
	setAttr -s 19 ".cp[0:18]" -type "double3" -2 -4 0 -1.9999999999999982 
		0 0 -2 -4 0 -1.9999999999999991 0 0 -1.9999999999999991 -4 0 -1.9999999999999982 
		0 0 -1.9999999999999991 -4 0 -1.9999999999999991 0 0 -2 -4 0 -1.9999999999999982 
		0 0 -2 -4 0 -1.9999999999999982 0 0 -1.9999999999999991 -4 0 -1.9999999999999982 
		0 0 -1.9999999999999991 -4 0 -1.9999999999999991 0 0 0 0 0 0 0 0 0 0 0;
createNode parentConstraint -n "ct_head_icon_parentConstraint1" -p "ct_head_icon";
	rename -uid "61810C6F-9440-1C1D-5E52-EBBC2967CA7F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ct_head_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -4.4408920985006262e-16 17.412103036884318 
		7.0253325276343208 ;
	setAttr ".rst" -type "double3" 1.9999999999999998 108.47364173317335 8.2524299197165352 ;
	setAttr -k on ".w0";
createNode transform -n "lt_fingers_icon" -p "icon_grp";
	rename -uid "394356FE-E143-7D9F-F024-9C8D90D030F0";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".s" -type "double3" 0.78603008501079685 0.78603008501079685 0.78603008501079685 ;
	setAttr ".rp" -type "double3" -4.9769975322816464e-14 2.9932536356048018e-14 0 ;
	setAttr ".sp" -type "double3" -6.3318155719361312e-14 3.8080649744642869e-14 0 ;
	setAttr ".spt" -type "double3" 1.3548180396544859e-14 -8.1481133885948517e-15 0 ;
createNode nurbsCurve -n "lt_fingers_iconShape" -p "lt_fingers_icon";
	rename -uid "003E3941-C245-46E3-6688-A6BDA1BE9073";
	setAttr -k off ".v";
	setAttr ".tw" yes;
	setAttr -s 19 ".cp[0:18]" -type "double3" -7.1054273576010019e-15 -1.9984014443252818e-15 
		-6 -7.1054273576010019e-15 -3.2862601528904634e-14 -2 -7.1054273576010019e-15 -1.9984014443252818e-15 
		-4.4408920985006262e-16 -7.1054273576010019e-15 -5.8841820305133297e-15 -4.4408920985006262e-16 
		-7.1054273576010019e-15 9.4368957093138306e-15 -8.8817841970012523e-16 -7.1054273576010019e-15 
		-3.4717003857093176e-15 0 -7.1054273576010019e-15 -1.6375789613221059e-14 -4.4408920985006262e-16 
		-7.1054273576010019e-15 -1.2212453270876722e-15 -4.4408920985006262e-16 -7.1054273576010019e-15 
		-5.1070259132757201e-15 -4.4408920985006262e-16 -7.1054273576010019e-15 -1.2656542480726785e-14 
		-2 -7.1054273576010019e-15 -5.1070259132757201e-15 -6 -7.1054273576010019e-15 -1.2212453270876722e-15 
		-6 -7.1054273576010019e-15 -1.6375789613221059e-14 -6 -7.1054273576010019e-15 -3.4717003857093176e-15 
		-5.9999999999999991 -7.1054273576010019e-15 9.4368957093138306e-15 -6 -7.1054273576010019e-15 
		-5.8841820305133297e-15 -6 0 0 0 0 0 0 0 0 0;
createNode transform -n "lt_index_ik_icon" -p "lt_fingers_icon";
	rename -uid "D374F61D-C84B-CB80-6F9D-AF97AF3D8564";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".s" -type "double3" 1 0.6 0.6 ;
	setAttr ".rp" -type "double3" -60.880079239346934 -104.91050269680487 2.2277521905716933 ;
	setAttr ".sp" -type "double3" -60.880079239346934 -174.85083782800803 3.712920317619488 ;
	setAttr ".spt" -type "double3" 0 69.940335131203213 -1.4851681270477952 ;
createNode nurbsCurve -n "lt_index_ik_iconShape" -p "lt_index_ik_icon";
	rename -uid "2D5D8FA2-644A-E410-5684-758A3683FED5";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "lt_middle_ik_icon" -p "lt_fingers_icon";
	rename -uid "17FCD7B5-0D4D-2E26-35C0-94AD037EA688";
	setAttr ".ove" yes;
	setAttr ".ovc" 27;
	setAttr ".s" -type "double3" 1 0.6 0.6 ;
	setAttr ".rp" -type "double3" -60.880079239346934 -104.91050269680487 0.22775219057169155 ;
	setAttr ".sp" -type "double3" -60.880079239346934 -174.85083782800803 0.37958698428615306 ;
	setAttr ".spt" -type "double3" 0 69.940335131203213 -0.15183479371446121 ;
createNode nurbsCurve -n "lt_middle_ik_iconShape" -p "lt_middle_ik_icon";
	rename -uid "6098A581-4B46-2479-B92C-2DA09D466300";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "lt_ring_ik_icon" -p "lt_fingers_icon";
	rename -uid "0C9895B9-A048-F0DD-5EF3-F3ADF9E3984A";
	setAttr ".ove" yes;
	setAttr ".ovc" 28;
	setAttr ".s" -type "double3" 1 0.6 0.6 ;
	setAttr ".rp" -type "double3" -60.880079239346934 -104.91050269680487 -1.7722478094283087 ;
	setAttr ".sp" -type "double3" -60.880079239346934 -174.85083782800803 -2.9537463490471811 ;
	setAttr ".spt" -type "double3" 0 69.940335131203213 1.1814985396188729 ;
createNode nurbsCurve -n "lt_ring_ik_iconShape" -p "lt_ring_ik_icon";
	rename -uid "ABE33183-8040-5D1A-8E93-09888648E31A";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "lt_pinky_ik_icon" -p "lt_fingers_icon";
	rename -uid "D71936E6-3B42-1E45-E316-01BF68BA11F4";
	setAttr ".ove" yes;
	setAttr ".ovc" 30;
	setAttr ".s" -type "double3" 1 0.6 0.6 ;
	setAttr ".rp" -type "double3" -60.880079239346934 -104.91050269680487 -3.7722478094283094 ;
	setAttr ".sp" -type "double3" -60.880079239346934 -174.85083782800803 -6.2870796823805168 ;
	setAttr ".spt" -type "double3" 0 69.940335131203213 2.5148318729522066 ;
createNode nurbsCurve -n "lt_pinky_ik_iconShape" -p "lt_pinky_ik_icon";
	rename -uid "3BFF600B-734A-7EF6-E778-C4B615FBA111";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "lt_fingers_icon_parentConstraint1" -p "lt_fingers_icon";
	rename -uid "575F8B38-DC41-F70D-DEF4-B4AF13718197";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_hand_01_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 2.8297640775457253 3.7937008351887314 0.87459895453736136 ;
	setAttr ".rst" -type "double3" 43.001478860260619 83.85912289329417 0.60701001129433463 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "lt_arm_hybrid_icon_orientConstraint1" -p "icon_grp";
	rename -uid "6EA8BC09-6444-3A21-DCDB-E292FDFD4DC0";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lt_arm_02_locW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 25.346616744995117 79.589035034179688 -31.316776427345978 ;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr ".s" -type "double3" 3.2674839585079725 3.2674839585079725 3.2674839585079725 ;
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "ECDE828A-F448-6FF3-21DE-AA95E64A0D5B";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode displayLayerManager -n "layerManager";
	rename -uid "EE5C3E0D-B147-0818-1340-FBBBE6B2C5FE";
createNode displayLayer -n "defaultLayer";
	rename -uid "56B97998-E24C-3ADE-0881-26BC9E9F4BD1";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "B6C28AFE-5441-F60C-8E96-23858663228C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "0E2F6C42-BA42-F095-0EA9-7AA7C89AA060";
	setAttr ".g" yes;
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "A0BA4E87-564D-EC41-198C-ED8BE027A784";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "820C1F2A-5F4A-969A-C144-F38C8375EA65";
createNode rmanGlobals -s -n "rmanGlobals";
	rename -uid "B6B37DF6-D840-D172-5471-31AE9B1DFAAE";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".hider_minSamples" 0;
	setAttr ".hider_maxSamples" 128;
	setAttr ".ri_pixelVariance" 0.014999999664723873;
	setAttr ".hider_incremental" yes;
	setAttr ".ipr_hider_maxSamples" 64;
	setAttr ".ipr_ri_pixelVariance" 0.05000000074505806;
	setAttr ".ipr_ri_decidither" 0;
	setAttr ".ri_maxSpecularDepth" 4;
	setAttr ".ri_maxDiffuseDepth" 1;
	setAttr ".ri_displayFilter" -type "string" "gaussian";
	setAttr ".ri_displayFilterSize" -type "float2" 2 2 ;
	setAttr ".motionBlur" 0;
	setAttr ".cameraBlur" no;
	setAttr ".shutterAngle" 180;
	setAttr ".shutterOpenEnd" 0;
	setAttr ".shutterCloseStart" 1;
	setAttr ".shutterTiming" 0;
	setAttr ".motionSamples" 2;
	setAttr ".displayFilters[0]" -type "string" "";
	setAttr ".sampleFilters[0]" -type "string" "";
	setAttr ".outputAllShaders" no;
	setAttr ".reentrantProcedurals" yes;
	setAttr ".outputShadowAOV" 0;
	setAttr ".enableImagePlaneFilter" yes;
	setAttr ".learnLightSelection" yes;
	setAttr ".opt_bucket_order" -type "string" "circle";
	setAttr ".limits_bucketsize" -type "long2" 16 16 ;
	setAttr ".limits_othreshold" -type "float3" 0.99599999 0.99599999 0.99599999 ;
	setAttr ".rfm_referenceFrame" 0;
	setAttr ".adaptiveMetric" -type "string" "variance";
	setAttr ".hider_darkfalloff" 0.02500000037252903;
	setAttr ".hider_exposurebracket" -type "float2" -1 1 ;
	setAttr ".ri_hider_adaptAll" no;
	setAttr ".dice_micropolygonlength" 1;
	setAttr ".dice_watertight" no;
	setAttr ".dice_referenceCameraType" 0;
	setAttr ".dice_referenceCamera" -type "string" "";
	setAttr ".hair_minWidth" 0.5;
	setAttr ".trace_autobias" yes;
	setAttr ".trace_bias" 0.0010000000474974513;
	setAttr ".trace_worldorigin" -type "string" "camera";
	setAttr ".trace_worldoffset" -type "float3" 0 0 0 ;
	setAttr ".opt_oslSIMDEnable" yes;
	setAttr ".opt_oslVerbosity" 0;
	setAttr ".opt_oslStatistics" 0;
	setAttr ".deep_quality" 0.75;
	setAttr ".opt_cropWindowEnable" no;
	setAttr ".opt_cropWindowTopLeft" -type "float2" 0 0 ;
	setAttr ".opt_cropWindowBottomRight" -type "float2" 1 1 ;
	setAttr ".user_sceneUnits" 1;
	setAttr ".user_iesIgnoreWatts" yes;
	setAttr ".limits_texturememory" 4096;
	setAttr ".limits_geocachememory" 4096;
	setAttr ".limits_opacitycachememory" 2048;
	setAttr ".statistics_level" 1;
	setAttr ".statistics_xmlfilename" -type "string" "";
	setAttr ".lpe_reload_definitions" -type "string" "";
	setAttr ".lpe_diffuse2" -type "string" "Diffuse,HairDiffuse";
	setAttr ".lpe_diffuse3" -type "string" "Subsurface";
	setAttr ".lpe_specular2" -type "string" "Specular,HairSpecularR";
	setAttr ".lpe_specular3" -type "string" "RoughSpecular,HairSpecularTRT";
	setAttr ".lpe_specular4" -type "string" "Clearcoat";
	setAttr ".lpe_specular5" -type "string" "Iridescence";
	setAttr ".lpe_specular6" -type "string" "Fuzz,HairSpecularGLINTS";
	setAttr ".lpe_specular7" -type "string" "SingleScatter,HairSpecularTT";
	setAttr ".lpe_specular8" -type "string" "Glass";
	setAttr ".lpe_user2" -type "string" "Albedo,DiffuseAlbedo,SubsurfaceAlbedo,HairAlbedo";
	setAttr ".lpe_user3" -type "string" "Position";
	setAttr ".lpe_user4" -type "string" "UserColor";
	setAttr ".lpe_user5" -type "string" "";
	setAttr ".lpe_user6" -type "string" "Normal,DiffuseNormal,HairTangent,SubsurfaceNormal,SpecularNormal,RoughSpecularNormal,SingleScatterNormal,FuzzNormal,IridescenceNormal,GlassNormal";
	setAttr ".lpe_user7" -type "string" "";
	setAttr ".lpe_user8" -type "string" "";
	setAttr ".lpe_user9" -type "string" "";
	setAttr ".lpe_user10" -type "string" "";
	setAttr ".lpe_user11" -type "string" "";
	setAttr ".lpe_user12" -type "string" "";
	setAttr ".imageFileFormat" -type "string" "<scene>_<layer>_<camera>_<aov>.<f4>.<ext>";
	setAttr ".ribFileFormat" -type "string" "<camera><layer>.<f4>.rib";
	setAttr ".version" 1;
	setAttr ".take" 1;
	setAttr ".imageOutputDir" -type "string" "<ws>/images/<scene>_v<version>_t<take>";
	setAttr ".ribOutputDir" -type "string" "<ws>/renderman/rib/<scene>/v<version>_t<take>";
	setAttr -s 10 ".UserTokens";
	setAttr ".UserTokens[0].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[0].userTokenValues" -type "string" "";
	setAttr ".UserTokens[1].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[1].userTokenValues" -type "string" "";
	setAttr ".UserTokens[2].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[2].userTokenValues" -type "string" "";
	setAttr ".UserTokens[3].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[3].userTokenValues" -type "string" "";
	setAttr ".UserTokens[4].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[4].userTokenValues" -type "string" "";
	setAttr ".UserTokens[5].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[5].userTokenValues" -type "string" "";
	setAttr ".UserTokens[6].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[6].userTokenValues" -type "string" "";
	setAttr ".UserTokens[7].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[7].userTokenValues" -type "string" "";
	setAttr ".UserTokens[8].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[8].userTokenValues" -type "string" "";
	setAttr ".UserTokens[9].userTokenKeys" -type "string" "";
	setAttr ".UserTokens[9].userTokenValues" -type "string" "";
	setAttr ".rlfData" -type "string" "init";
	setAttr ".jobid" -type "string" "";
createNode PxrPathTracer -s -n "PxrPathTracer";
	rename -uid "803B4F62-7640-A3B2-1C38-4FBAAE58FC45";
	setAttr ".cch" no;
	setAttr ".fzn" no;
	setAttr ".ihi" 2;
	setAttr ".nds" 0;
	setAttr ".maxIndirectBounces" 8;
	setAttr ".maxContinuationLength" -1;
	setAttr ".maxNonStochasticOpacityEvents" 0;
	setAttr ".sampleMode" -type "string" "bxdf";
	setAttr ".numLightSamples" 1;
	setAttr ".numBxdfSamples" 1;
	setAttr ".numIndirectSamples" 1;
	setAttr ".numDiffuseSamples" 1;
	setAttr ".numSpecularSamples" 1;
	setAttr ".numSubsurfaceSamples" 1;
	setAttr ".numRefractionSamples" 1;
	setAttr ".allowCaustics" no;
	setAttr ".accumOpacity" no;
	setAttr ".rouletteDepth" 4;
	setAttr ".rouletteThreshold" 0.20000000298023224;
	setAttr ".clampDepth" 2;
	setAttr ".clampLuminance" 10;
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "7232243A-1C4D-1053-7BBA-8C938F4231DE";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry1";
	rename -uid "8B9008B8-F141-B3AF-AB35-F0952B4527F4";
	setAttr ".txf" -type "matrix" 26.326178358287397 0 0 0 0 26.326178358287397 0 0
		 0 0 26.326178358287397 0 0 1.5608462488677652e-31 0.69654588338797963 1;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "9F78F1C7-5547-7C0C-7FD0-209EE9673937";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 0\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 603\n            -height 346\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1219\n            -height 740\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 0\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 603\n            -height 345\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 16384\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 787\n            -height 740\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n"
		+ "            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n"
		+ "            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n"
		+ "            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n"
		+ "            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n"
		+ "                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 1\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 1\n                -autoFitTime 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showResults \"off\" \n                -showBufferCurves \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -showCurveNames 0\n                -showActiveCurveNames 0\n                -stackedCurves 0\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -displayNormalized 0\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -classicMode 1\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 1\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n"
		+ "                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n"
		+ "                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayKeys 1\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayKeys 0\n                -displayTangents 0\n                -displayActiveKeys 0\n                -displayActiveKeyTangents 0\n                -displayInfinities 0\n                -displayValues 0\n                -autoFit 0\n                -autoFitTime 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 1\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 1\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 1\n                -showInvisible 1\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n"
		+ "                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n"
		+ "                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 16384\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -rendererOverrideName \"stereoOverrideVP2\" \n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n"
		+ "                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n"
		+ "                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n"
		+ "                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 787\\n    -height 740\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 16384\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 787\\n    -height 740\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A1E58205-2448-E458-B76F-7C83E1141AB5";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 200 -ast -10 -aet 200 ";
	setAttr ".st" 6;
createNode makeNurbCircle -n "makeNurbCircle2";
	rename -uid "1C81FE58-674C-0B69-3445-8D8C9150E921";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode transformGeometry -n "transformGeometry2";
	rename -uid "15B7A817-FD4D-EC85-A4F7-7A8A0970BC50";
	setAttr ".txf" -type "matrix" 1 0 -7.3955709864469857e-32 0 -2.7755575615628914e-17 0.99999999999999978 -9.8607613152626476e-32 0
		 1.2325951644078309e-32 0 1 0 -7.7502790993724284 0.99122288235885403 -1.3193100098274115 1;
createNode transformGeometry -n "transformGeometry3";
	rename -uid "3AADCFF9-C64F-EF5D-EB0F-7E8400D833DB";
	setAttr ".txf" -type "matrix" 4.4408920985006262e-16 -0.98447056858451232 0.17554970689490393 0
		 2.7755575615628904e-16 0.17554970689490398 0.98447056858451232 0 -1 -2.7755575615628904e-16 4.4408920985006262e-16 0
		 7.5387029824302356e-16 -2.4016318926383721e-15 -9.2184925667451338e-16 1;
createNode makeNurbCircle -n "makeNurbCircle4";
	rename -uid "4EF4539F-964B-4289-F6FB-24B2DD5256C0";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle5";
	rename -uid "E53EBAD7-2D47-43C1-AA2B-D5A8A756B5EE";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle6";
	rename -uid "BF17657B-2E4A-D4FF-C703-D18608E98D77";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry6";
	rename -uid "253EB5B9-C040-A9FB-7E4B-66B5C5BCADC5";
	setAttr ".txf" -type "matrix" 5.8489269999999998 0 0 0 0 5.8489269999999998 0 0
		 0 0 5.8489269999999998 0 0 0 0 1;
createNode transformGeometry -n "transformGeometry7";
	rename -uid "F451803E-BE40-701B-A290-82B98FA97375";
	setAttr ".txf" -type "matrix" 2.0474890000000006 0 0 0 0 2.0474890000000006 0 0
		 0 0 2.0474890000000006 0 4.0000000000000009 0 0 1;
createNode transformGeometry -n "transformGeometry8";
	rename -uid "F69619C7-3047-2F66-1A32-A08F78F1FBC1";
	setAttr ".txf" -type "matrix" 2.0474890000000006 0 0 0 0 2.0474890000000006 0 0
		 0 0 2.0474890000000006 0 -4.0000000000000009 0 0 1;
createNode transformGeometry -n "transformGeometry9";
	rename -uid "FCA3A026-0542-B62F-E31E-A0A17EA9AA6D";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1.0000000000000002 0
		 0 1.0000000000000002 2.2204460492503131e-16 0 0 0 0 1;
createNode transformGeometry -n "transformGeometry10";
	rename -uid "BFA3877F-8B4E-619F-7B07-6587C19EA819";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1.0000000000000002 0
		 0 1.0000000000000002 2.2204460492503131e-16 0 0 0 0 1;
createNode transformGeometry -n "transformGeometry11";
	rename -uid "EB2771B3-B04A-5C0F-EF7E-0593382A0381";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 2.2204460492503131e-16 -1.0000000000000002 0
		 0 1.0000000000000002 2.2204460492503131e-16 0 0 0 0 1;
createNode transformGeometry -n "transformGeometry12";
	rename -uid "E55199E8-0141-CFA2-7F0F-45B04B1D2FBA";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.0000000000000009 0 0 1;
createNode transformGeometry -n "transformGeometry13";
	rename -uid "58DE4ADA-EE4F-80A7-9E52-9DBEDF710DEA";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.0000000000000009 0 0 1;
createNode transformGeometry -n "transformGeometry14";
	rename -uid "816CFA2B-D549-E930-83FD-FAAD71003C49";
	setAttr ".txf" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 0 0 0 1;
createNode transformGeometry -n "transformGeometry15";
	rename -uid "8B7D73D4-724F-18BE-23D5-41B16AF9C53D";
	setAttr ".txf" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 0 0 0 1;
createNode transformGeometry -n "transformGeometry16";
	rename -uid "4D6418A8-2E49-C34E-FD31-D2B2A4423B9A";
	setAttr ".txf" -type "matrix" -1 0 -1.2246467991473532e-16 0 0 1 0 0 1.2246467991473532e-16 0 -1 0
		 0 0 0 1;
createNode makeNurbCircle -n "makeNurbCircle7";
	rename -uid "37313AF0-EF49-8EDD-276D-5797F6D457FA";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".r" 8;
	setAttr ".s" 16;
createNode transformGeometry -n "transformGeometry17";
	rename -uid "0E636814-C24F-7468-230D-F78AFE13C98B";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 110.47364173317335 1.631442575104577e-14 8.2524299197165334 1;
createNode transformGeometry -n "transformGeometry18";
	rename -uid "C4AA6075-1044-E292-0F3C-2AA89C411773";
	setAttr ".txf" -type "matrix" 2.2204460492503131e-16 1 0 0 -1 2.2204460492503131e-16 0 0
		 0 0 1 0 6.4392935428259079e-15 -3.6225302204697151e-30 0 1;
createNode transformGeometry -n "transformGeometry19";
	rename -uid "7B4760E8-6242-231F-7B7C-9F94721F8939";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 100.25115966796875 31.718500929572123 1;
createNode transformGeometry -n "transformGeometry20";
	rename -uid "BEFC355E-1341-93F2-D757-F6B47B9A37EE";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 100.25115966796875 31.718500929572123 1;
createNode transformGeometry -n "transformGeometry21";
	rename -uid "21331452-B345-DC91-50F7-888EEBFCAA76";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 100.25115966796875 31.718500929572123 1;
createNode controller -n "ct_hip_loc_tag";
	rename -uid "FC55FCE4-764D-6F77-9F53-2CA4A354E911";
	setAttr -s 2 ".child";
createNode controller -n "lt_leg_01_loc_tag";
	rename -uid "2E68F704-AF4E-49C4-53CF-0990D51C30AE";
createNode controller -n "lt_leg_02_loc_tag";
	rename -uid "171CD692-574F-EFC1-2F05-4B9109311004";
createNode controller -n "lt_leg_03_loc_tag";
	rename -uid "2685BD72-AA41-2DEC-6624-AA82A5E8023B";
createNode controller -n "lt_leg_04_loc_tag";
	rename -uid "3D9B8053-E045-BDCE-DADB-45BC932453D8";
	setAttr -s 5 ".child";
createNode controller -n "lt_toeA_01_loc_tag";
	rename -uid "44AB5EA3-414F-5410-D065-64BA0E9C9F88";
createNode controller -n "lt_toeA_02_loc_tag";
	rename -uid "DDEADB9E-B542-5E81-DE94-33A4BBEFC616";
createNode controller -n "lt_toeA_03_loc_tag";
	rename -uid "7EFA4B01-494D-F959-9901-9590F61D6894";
createNode controller -n "lt_toeB_01_loc_tag";
	rename -uid "9039F547-C645-604F-D22C-669CA7703595";
createNode controller -n "lt_toeB_02_loc_tag";
	rename -uid "2578F116-184A-0023-2120-30A57CBDAB04";
createNode controller -n "lt_toeB_03_loc_tag";
	rename -uid "39C5D094-7349-28DC-F42B-A4A62B65D91A";
createNode controller -n "lt_toeC_01_loc_tag";
	rename -uid "01787FCB-EA4A-C1D7-3E84-6F833640A838";
createNode controller -n "lt_toeC_02_loc_tag";
	rename -uid "1CA57294-B54B-F44B-A6DC-92AEC443755F";
createNode controller -n "lt_toeC_03_loc_tag";
	rename -uid "B33063FD-514B-3C9E-C759-A9802A40B023";
createNode controller -n "lt_toeD_01_loc_tag";
	rename -uid "1BF20F6C-6E47-553E-8A96-8FAD8FC4A0D0";
createNode controller -n "lt_toeD_02_loc_tag";
	rename -uid "67FC63CA-D04A-0864-A118-74893BD65701";
createNode controller -n "lt_toeD_03_loc_tag";
	rename -uid "6132B622-6A48-DA53-6F96-8993B8A9AB30";
createNode controller -n "lt_toeE_01_loc_tag";
	rename -uid "73131F95-ED40-183A-1651-A59B12F1C9D9";
createNode controller -n "lt_toeE_02_loc_tag";
	rename -uid "BB0CA3B9-E440-8C44-75C7-29A4A39360FC";
createNode controller -n "lt_toeE_03_loc_tag";
	rename -uid "5A01A8C5-474E-22D2-8452-89B147D4DD95";
createNode controller -n "ct_back_01_loc_tag";
	rename -uid "9290ADDC-5545-4B3C-E410-3FB82039198E";
createNode controller -n "ct_back_02_loc_tag";
	rename -uid "EC65BDD6-3A40-D6D6-B9F2-C39E21D6D4C7";
createNode controller -n "ct_back_03_loc_tag";
	rename -uid "303BAA5B-9045-9975-C445-F887DBFBE97B";
createNode controller -n "ct_back_04_loc_tag";
	rename -uid "80D0BC45-2D4C-6AAE-10CF-EBB0A825E244";
createNode controller -n "ct_back_05_loc_tag";
	rename -uid "51790B78-024C-8D25-A322-9AAFFA27897E";
	setAttr -s 2 ".child";
createNode controller -n "ct_back_06_loc_tag";
	rename -uid "F5BBA6AA-FA43-43D8-2D3C-6F9380667A46";
createNode controller -n "ct_back_07_loc_tag";
	rename -uid "D9D45377-6044-720B-9602-E99F4BA3436C";
createNode controller -n "ct_neck_01_loc_tag";
	rename -uid "8C8587D8-0342-16BF-39E3-0C91755BCAEA";
createNode controller -n "ct_neck_02_loc_tag";
	rename -uid "7D2E8715-9840-5C75-7B2E-4B806710BECC";
createNode controller -n "ct_neck_03_loc_tag";
	rename -uid "DE16734A-494D-C080-0BCE-F1814282A4EC";
createNode controller -n "ct_neck_04_loc_tag";
	rename -uid "397C1842-A942-EC12-5961-B4B3F6534F0E";
createNode controller -n "ct_head_01_loc_tag";
	rename -uid "C25864E9-1546-BC28-DB9C-F09BC462F26D";
	setAttr -s 3 ".child";
createNode controller -n "ct_head_02_loc_tag";
	rename -uid "EDF9D462-C244-E8DC-9275-02A59EB41E25";
createNode controller -n "lt_eye_01_loc_tag";
	rename -uid "6357C038-CA4E-D6E0-391B-BD82CFC9DA42";
createNode controller -n "lt_eye_02_loc_tag";
	rename -uid "02592862-C747-8A22-69BC-CB8C9F12DD2F";
createNode controller -n "ct_jaw_01_loc_tag";
	rename -uid "D365C3CA-4943-7408-27C2-0CA16737B048";
createNode controller -n "ct_jaw_02_loc_tag";
	rename -uid "DEB24F27-7D47-E62F-F6E3-E3877221FD95";
createNode controller -n "lt_clav_01_loc_tag";
	rename -uid "7E57055A-E941-F8A4-8F2B-AC889FF92B58";
createNode controller -n "lt_clav_02_loc_tag";
	rename -uid "0B39B66A-2746-D2FC-4FF7-9C9487363AD2";
createNode controller -n "lt_arm_01_loc_tag";
	rename -uid "D1760F5F-4E4B-D307-D481-E786D59D0123";
createNode controller -n "lt_arm_02_loc_tag";
	rename -uid "C44CE992-454C-5FED-202D-1E8CEF10F2C3";
createNode controller -n "lt_arm_03_loc_tag";
	rename -uid "A806C259-2040-B7DB-2057-4BB8F26A589C";
createNode controller -n "lt_hand_01_loc_tag";
	rename -uid "48ED443B-7540-D7E2-FD7A-B49D18C30410";
createNode controller -n "lt_hand_02_loc_tag";
	rename -uid "2A6882CE-954F-EA06-9920-0B862DF7E755";
	setAttr -s 5 ".child";
createNode controller -n "lt_thumb_01_pivot_loc_tag";
	rename -uid "EDC567CA-0E4F-A8F0-B98C-8291CC4F5761";
createNode controller -n "lt_thumb_02_loc_tag";
	rename -uid "0CF71BC3-1E44-C536-A7B4-C0AB9FF94C5C";
createNode controller -n "lt_thumb_03_loc_tag";
	rename -uid "8883383C-ED46-B863-C154-80B6A5F663BA";
createNode controller -n "lt_thumb_04_loc_tag";
	rename -uid "9D5C98DF-7343-BCBB-B27C-91A792E02F2E";
createNode controller -n "lt_thumb_05_loc_tag";
	rename -uid "E3CAF8C4-724D-0759-30A2-8ABB05AE7C81";
createNode controller -n "lt_middle_01_loc_tag";
	rename -uid "611E2D6B-134F-62DB-429C-7C8DC4672A40";
createNode controller -n "lt_middle_02_loc_tag";
	rename -uid "15D7CB0F-1F44-3000-FFA2-8CB2A6F92600";
createNode controller -n "lt_middle_03_loc_tag";
	rename -uid "A1B58E38-9C4C-8055-E5CD-F5880763F549";
createNode controller -n "lt_middle_04_loc_tag";
	rename -uid "C0B873D3-4846-96F8-4601-7EB949FA97CF";
createNode controller -n "lt_middle_05_loc_tag";
	rename -uid "2EB91527-CD44-56CB-8E06-7BA0078A8D39";
createNode controller -n "lt_ring_01_loc_tag";
	rename -uid "8F6FBCD7-EF4D-5742-42CC-BF85EDAE64A4";
createNode controller -n "lt_ring_02_loc_tag";
	rename -uid "FE1E1544-044E-6AC4-43D4-15837D761156";
createNode controller -n "lt_ring_03_loc_tag";
	rename -uid "1B0B4B0F-A943-DA6C-7760-6F901C643C6C";
createNode controller -n "lt_ring_04_loc_tag";
	rename -uid "BB24F761-A745-7270-19D5-D7959D0CCA76";
createNode controller -n "lt_ring_05_loc_tag";
	rename -uid "4B8A2B2A-EE45-7200-5117-A18D2BEFC79E";
createNode controller -n "lt_pinky_01_loc_tag";
	rename -uid "57A294DA-EC46-2B34-1366-F79E3E0BEF33";
createNode controller -n "lt_pinky_02_loc_tag";
	rename -uid "71C0964A-1C42-9B63-035B-3689607FBD1A";
createNode controller -n "lt_pinky_03_loc_tag";
	rename -uid "78071E6E-1145-DAE6-42E2-C5A3458DFE72";
createNode controller -n "lt_pinky_04_loc_tag";
	rename -uid "8D36383B-2448-7FD2-A3D8-42AD743A46FD";
createNode controller -n "lt_pinky_05_loc_tag";
	rename -uid "33392B09-BC4B-834A-D70B-DB915B42CF9B";
createNode controller -n "lt_index_01_loc_tag";
	rename -uid "34A600AB-6848-ABA9-B025-ACA270FD21C4";
createNode controller -n "lt_index_02_loc_tag";
	rename -uid "55E81304-F246-6418-6E10-18ACFEFD08AB";
createNode controller -n "lt_index_03_loc_tag";
	rename -uid "9F6FF722-C34C-7B22-674C-38B25B1DA2D6";
createNode controller -n "lt_index_04_loc_tag";
	rename -uid "98C778EC-5D4B-5C79-5065-61BE1F277C02";
createNode controller -n "lt_index_05_loc_tag";
	rename -uid "B8D0F407-654F-85E4-10AA-B3A07160015B";
createNode controller -n "lt_leg_04_fk_icon_tag";
	rename -uid "B4E015BB-FD4C-C717-68F3-67803FB7DEDF";
createNode controller -n "lt_leg_03_fk_icon_tag";
	rename -uid "CF914F64-3145-A246-D045-3983CCE6784C";
createNode controller -n "lt_leg_02_fk_icon_tag";
	rename -uid "C18C7306-DD4A-CEB1-F6E7-8391F5F6190A";
createNode controller -n "lt_leg_01_fk_icon_tag";
	rename -uid "F73E7AF2-394C-5635-852A-8BB4B275850C";
createNode controller -n "ct_hip_icon_tag";
	rename -uid "514EE2EA-5A49-D9B6-342C-0886E69AC6AA";
createNode makeNurbCircle -n "makeNurbCircle8";
	rename -uid "B95AA171-4B4D-052D-E3AE-4DA125D0F4E6";
	setAttr ".nr" -type "double3" 0 1 0 ;
	setAttr ".s" 16;
createNode transformGeometry -n "transformGeometry22";
	rename -uid "93C1CE04-544A-FF10-274D-FF927FFFB558";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.6653345369377348e-16 47.962421417236328 -2.1840825080871582 1;
createNode makeNurbCircle -n "makeNurbCircle9";
	rename -uid "FFC08FA1-854B-319B-F1BF-8EB8B14D6C9A";
createNode transformGeometry -n "transformGeometry23";
	rename -uid "7BCF4B89-6543-A73D-89BA-E0BB10B99979";
	setAttr ".txf" -type "matrix" 1 -2.1684043449710089e-19 0 0 -2.1684043449710089e-19 0.99999999999999989 1.2621774483536189e-29 0
		 0 -1.2621774483536189e-29 1 0 61.35204542004336 -2.4429314013110988 2.4501708430014468e-13 1;
createNode transformGeometry -n "transformGeometry24";
	rename -uid "41D3B931-954C-1F23-E9D5-ACB00E9CC17D";
	setAttr ".txf" -type "matrix" 4.4408920985006262e-16 0.99999812044283687 0.0019388426428802448 0
		 1.1135536936990318e-13 -0.0019388426428801342 0.99999812044283676 0 1.0000000000000002 -2.7755575615628909e-16 -1.1146639167236572e-13 0
		 -2.8651046565488298e-14 2.3184579256430705e-15 6.6613381477782504e-15 1;
createNode makeNurbCircle -n "makeNurbCircle10";
	rename -uid "BF3A5A06-DD40-C220-6D5A-99B0023E8316";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode transformGeometry -n "transformGeometry25";
	rename -uid "8F509AB9-7B49-B8E4-B0D3-9FB7AFEC492F";
	setAttr ".txf" -type "matrix" 1 -4.3368086899420177e-19 -2.7755575615628914e-17 0
		 -1.3010426069826053e-18 0.99999999999999989 0 0 -2.7755575615628914e-17 0 0.99999999999999989 0
		 8.229125784895821 -79.75078381110383 0.51318821568740236 1;
createNode transformGeometry -n "transformGeometry26";
	rename -uid "19EA5F8B-E84C-FDC0-5E38-97ADB971B458";
	setAttr ".txf" -type "matrix" 0.98946737316456856 -0.0063585809598554928 -0.14461634033187767 0
		 -0.0062917355929504332 -0.99997978401974597 0.0009195732985670408 0 -0.14461926395206451 -3.7709966442880948e-13 -0.98948737662183639 0
		 -1.5543122344752192e-15 5.1414556772518982e-14 -6.6613381477509392e-16 1;
createNode makeNurbCircle -n "makeNurbCircle11";
	rename -uid "03285B62-E54B-3FB0-DD64-B1AB1BB13816";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry27";
	rename -uid "4FAC468F-7947-72BB-EA79-CDB9DEA7B22B";
	setAttr ".txf" -type "matrix" 1 1.6263032587282567e-19 0 0 2.7105054312137611e-19 1 0 0
		 -2.7755575615628914e-17 -4.3368086899420177e-19 1 0 10.762879849978011 -19.788837888613024 1.1379207818042683 1;
createNode transformGeometry -n "transformGeometry28";
	rename -uid "3167C6B3-2242-0EF7-3C0D-558A34F275E3";
	setAttr ".txf" -type "matrix" 0.99325790927344215 -0.025505473706905063 0.11308490826249509 0
		 -0.02534175760664191 -0.99967468248975166 -0.0028852227678001423 0 0.11312170873513519 -2.4184213659461668e-14 -0.99358113861568609 0
		 -3.1516906981929837e-16 -6.0983147993624042e-15 -2.1011271321286558e-16 1;
createNode makeNurbCircle -n "makeNurbCircle12";
	rename -uid "5ACD65F7-B34F-8EB1-8AF5-64B5750CCC74";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle13";
	rename -uid "D5A62DCE-6C49-1585-EE2B-3595E576B56E";
createNode transformGeometry -n "transformGeometry29";
	rename -uid "C7C45758-2241-DBE2-2AE5-8082BFFE9EB3";
	setAttr ".txf" -type "matrix" 1 0 0 0 2.7755575615628914e-17 1 0 0 0 0 1 0 -42.575868900083435 -7.3982238847310002 79.977188110351562 1;
createNode transformGeometry -n "transformGeometry30";
	rename -uid "FE498FF3-6641-CA06-93DD-078E7AABCFA6";
	setAttr ".txf" -type "matrix" 1 5.5511151231257827e-17 -5.5511151231257827e-17 0
		 -5.5511151231257827e-17 1 2.7755575615628914e-17 0 -5.5511151231257827e-17 -2.7755575615628914e-17 1 0
		 -22.627381540762016 80.782165470662761 -33.412387493422493 1;
createNode transformGeometry -n "transformGeometry31";
	rename -uid "5AFE4767-884A-A570-A8C6-1F826C099520";
	setAttr ".txf" -type "matrix" -0.97250728824095489 0 -0.23287244216141956 0 -0.23287244216141958 2.2204460492503131e-16 0.97250728824095511 0
		 4.163336342344337e-17 1 0 0 -3.55261870523129e-14 -1.4210854715202004e-14 1.4210854715202004e-14 1;
createNode transformGeometry -n "transformGeometry32";
	rename -uid "BAC2D2E4-8A49-1DCF-9411-0FA4A295FDF3";
	setAttr ".txf" -type "matrix" 0.45148839712483524 -0.54783978458850857 0.70429382908248161 0
		 0.29565891956478524 0.83658327166039881 0.4612095324901333 0 -0.84186936667361356 7.0776717819853745e-15 0.53968135918944715 0
		 0 9.108236687725391e-15 1.7763568394002505e-14 1;
createNode makeNurbCircle -n "makeNurbCircle14";
	rename -uid "F335DE10-B14A-251D-6102-D9B36FAA0198";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry33";
	rename -uid "53EE35A3-4A4C-9291-B82B-0780E206EA02";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 1.3501765263401646e-15 16.097463969618239 -0.27439824037472565 1;
createNode transformGeometry -n "transformGeometry34";
	rename -uid "9B55216D-1D44-821F-AC83-71A0EB48C303";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 2.7230566939403014e-15 0 1;
createNode makeNurbCircle -n "makeNurbCircle15";
	rename -uid "E2C8DED9-654E-2D12-EE11-FBB1C206709A";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry35";
	rename -uid "3A1D0B41-6240-BA44-082B-88BB69323ECF";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.4810191566552871 2.182234434656861 -3.3632022535504906 1;
createNode transformGeometry -n "transformGeometry36";
	rename -uid "B4213637-9A48-4945-2C28-97A5218DCCAC";
	setAttr ".txf" -type "matrix" 2.2204460492503131e-16 -1 0 0 1 2.2204460492503131e-16 0 0
		 0 0 1 0 -4.9878245805356326e-16 1.4229075156381449e-17 6.2347807256695408e-17 1;
createNode makeNurbCircle -n "makeNurbCircle16";
	rename -uid "046AAFDA-9D43-7755-3F33-1E9617608818";
	setAttr ".nr" -type "double3" 1 0 0 ;
	setAttr ".s" 16;
createNode makeNurbCircle -n "makeNurbCircle17";
	rename -uid "6AAEC696-684C-556B-53F8-D88599235F23";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode makeNurbCircle -n "makeNurbCircle18";
	rename -uid "682CE561-1444-F78C-4332-1B9AEBD2B926";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode makeNurbCircle -n "makeNurbCircle19";
	rename -uid "C4A3F0E1-7C4B-3022-4519-AC964EB1036A";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode makeNurbCircle -n "makeNurbCircle20";
	rename -uid "FFD9AEC5-0746-CB37-CA15-DE8F42DA7715";
	setAttr ".nr" -type "double3" 1 0 0 ;
createNode transformGeometry -n "transformGeometry37";
	rename -uid "A2A29B5A-BA4A-5EA4-1AD8-10B745DA7602";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 42.861177618940445 84.022193137669134 2.7324110567569728 1;
createNode transformGeometry -n "transformGeometry38";
	rename -uid "7A15CC2B-0E4F-7B9C-5137-C7AB2B99BCAA";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 42.861177618940445 140.03698856278189 4.5540184279282885 1;
createNode transformGeometry -n "transformGeometry39";
	rename -uid "0BC8004B-F14E-D5F3-7693-C39B3BDD962C";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 42.861177618940445 140.03698856278189 1.2206850945949548 1;
createNode transformGeometry -n "transformGeometry40";
	rename -uid "F9452B17-2E4E-A85D-FAB9-15BD0EE14847";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 42.861177618940445 140.03698856278189 -2.1126482387383789 1;
createNode transformGeometry -n "transformGeometry41";
	rename -uid "3C90AABC-9449-E456-8D54-F6949D32E464";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 42.861177618940445 140.03698856278189 -5.4459815720717124 1;
createNode transformGeometry -n "transformGeometry42";
	rename -uid "D81E88AD-5D48-897D-1878-289453F00A34";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -7.4014868308343773e-16 1;
createNode transformGeometry -n "transformGeometry43";
	rename -uid "151AF1B6-4E46-854A-5AE7-AEBFE50AAD79";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 11.667495565816505 22.872179914877592 -0.072841974537112872 1;
createNode transformGeometry -n "transformGeometry44";
	rename -uid "C6CAD461-064D-83F2-BA40-1DA513A25E00";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 11.667495565816505 38.120299858129322 -0.12140329089518813 1;
createNode transformGeometry -n "transformGeometry45";
	rename -uid "1145D5A4-AB44-4512-205F-9789CE0B89DC";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 11.667495565816505 38.120299858129322 -0.12140329089518813 1;
createNode transformGeometry -n "transformGeometry46";
	rename -uid "7C1B9507-FD44-D36A-E5AA-4A99662FEBA2";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 11.667495565816505 38.120299858129322 -0.12140329089518813 1;
createNode transformGeometry -n "transformGeometry47";
	rename -uid "06D09AB9-B540-7277-7F54-1B8797F155D8";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 11.667495565816505 38.120299858129322 -0.12140329089518813 1;
createNode transformGeometry -n "transformGeometry48";
	rename -uid "B19FC97D-414E-27F6-51B1-3DA85F7BD1F9";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.3374173879632363e-13 -7.4632666739019884e-17 1;
createNode transformGeometry -n "transformGeometry49";
	rename -uid "476373F3-2743-F8B6-C59E-84825E151369";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.9921814013520272e-13 -8.6453646098180424e-16 1;
createNode transformGeometry -n "transformGeometry50";
	rename -uid "7B0994F6-E44F-AF54-665C-19B7E1CBDCD9";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.9921814013520272e-13 -1.2438777789836649e-16 1;
createNode transformGeometry -n "transformGeometry51";
	rename -uid "ECD161C3-5445-74BD-878C-0598E30F2B81";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.9921814013520272e-13 -1.2438777789836649e-16 1;
createNode transformGeometry -n "transformGeometry52";
	rename -uid "E77A621A-A442-D59C-1422-BB8E61E261FD";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 1.9921814013520272e-13 -1.2438777789836649e-16 1;
createNode makeNurbCircle -n "makeNurbCircle21";
	rename -uid "830EA17D-7B46-0E98-F1D1-0199BEABF5BF";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode makeNurbCircle -n "makeNurbCircle22";
	rename -uid "70939CAB-3447-4021-97C6-56AB5C7B84BA";
	setAttr ".nr" -type "double3" 0 1 0 ;
createNode transformGeometry -n "transformGeometry53";
	rename -uid "23442274-C24E-6ECF-6B09-33BB5F668BA1";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -100.25115966796875 -31.718500929572123 1;
createNode transformGeometry -n "transformGeometry54";
	rename -uid "24A41B66-B242-6517-E6CA-0489F923F860";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -100.25115966796875 -31.718500929572123 1;
createNode transformGeometry -n "transformGeometry55";
	rename -uid "0AB83C2B-184A-CD35-B454-E48C2FB11880";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 -100.25115966796875 -31.718500929572123 1;
createNode transformGeometry -n "transformGeometry56";
	rename -uid "202B0551-A244-24DA-B439-42973BEE092E";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -1.4210854715202004e-14 -108.47364173317335 -8.2524299197165352 1;
createNode transformGeometry -n "transformGeometry57";
	rename -uid "8D8BF2A5-FD40-D93B-509C-17A12E01D9DD";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -54.528673184756947 -106.8943730525467 0.34043091778013945 1;
createNode transformGeometry -n "transformGeometry58";
	rename -uid "4E9EAD7A-8E47-2F0B-B55D-758729D82E06";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -54.528673184756947 -178.15728842091116 0.56738486296689916 1;
createNode transformGeometry -n "transformGeometry59";
	rename -uid "531FDFFE-C54D-5A90-0C40-018D84CEC76B";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -54.528673184756947 -178.15728842091116 0.56738486296689916 1;
createNode transformGeometry -n "transformGeometry60";
	rename -uid "EC0660DD-AB4C-8CB1-C280-248338ED66E5";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -54.528673184756947 -178.15728842091116 0.56738486296689916 1;
createNode transformGeometry -n "transformGeometry61";
	rename -uid "9F724E49-684E-571D-65A1-FAA4ED7CB186";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -54.528673184756947 -178.15728842091116 0.56738486296689916 1;
createNode transformGeometry -n "transformGeometry62";
	rename -uid "FEF691D2-1A46-9FDA-353D-72BFAFB67AFA";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -11.320523013883699 -19.507887884116162 -0.14359786006001599 1;
createNode transformGeometry -n "transformGeometry63";
	rename -uid "2F174300-FE45-18C8-BCEC-A78C534D372C";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6870869398161813e-14 -9.5529813425945458e-14 2.9853066695607954e-16 1;
createNode transformGeometry -n "transformGeometry64";
	rename -uid "76C18CBB-694C-ACA3-1B3A-55AB3D449EF9";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6870869398161813e-14 -1.5921635570990911e-13 -2.4259757148997181e-16 1;
createNode transformGeometry -n "transformGeometry65";
	rename -uid "79FE8E14-7846-951B-05D6-A2AE49AC33EB";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6870869398161813e-14 -1.5921635570990911e-13 4.5129181890075107e-16 1;
createNode transformGeometry -n "transformGeometry66";
	rename -uid "0CC321D4-054F-E48D-C80E-6D952461581C";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6870869398161813e-14 -1.5921635570990911e-13 1.2376997946769037e-15 1;
createNode transformGeometry -n "transformGeometry67";
	rename -uid "89B11447-8947-A66E-86B4-2C96C37495E9";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 -6.6870869398161813e-14 -1.5921635570990911e-13 -2.4259757148997181e-16 1;
createNode transformGeometry -n "transformGeometry68";
	rename -uid "594882F9-4E43-B206-300F-48A787ED3521";
	setAttr ".txf" -type "matrix" 1 -2.1684043449710089e-19 0 0 -2.1684043449710089e-19 1 -1.2621774483536189e-29 0
		 -4.9303806576313238e-32 1.2621774483536189e-29 1 0 5.635769854065507 -61.581072954405009 2.3239748477935929 1;
createNode transformGeometry -n "transformGeometry69";
	rename -uid "5AB2B9D7-3241-4798-DB21-AA932F5C8587";
	setAttr ".txf" -type "matrix" 4.4408920985006262e-16 0.99999812048845382 0.0019388191147528544 0
		 1.1352030426792226e-13 -0.0019388191147529099 0.99999812048845382 0 1 -2.7755575615628914e-16 -1.1346479311669101e-13 0
		 -4.6377209160981527e-30 -9.7443061469515365e-17 -3.6714442129904124e-16 1;
createNode controller -n "biped_ct_hip_loc_tag";
	rename -uid "57DCF193-844E-CCD2-661E-BB8971FBEE81";
	setAttr -s 2 ".child";
createNode controller -n "biped_lt_leg_01_loc_tag";
	rename -uid "CCACDCEF-A34B-53E7-680A-3ABBE13E4DFA";
createNode controller -n "biped_lt_leg_02_loc_tag";
	rename -uid "4534FAE2-A742-B95C-F0C1-B083422CF18C";
createNode controller -n "biped_lt_leg_03_loc_tag";
	rename -uid "A5CF974B-614D-9573-A56D-FA9061DBE482";
createNode controller -n "biped_lt_leg_04_loc_tag";
	rename -uid "1F09053D-724F-1BDD-5C53-F8BE6185AB44";
	setAttr -s 5 ".child";
createNode controller -n "biped_lt_toeA_01_loc_tag";
	rename -uid "7C476E3F-2844-B4DE-98F2-9A848B6E48DF";
createNode controller -n "biped_lt_toeA_02_loc_tag";
	rename -uid "12A29274-B647-F4F8-63FD-B4B6679B2C22";
createNode controller -n "biped_lt_toeA_03_loc_tag";
	rename -uid "0CB84038-EF47-6862-BCD4-BCA2B69B0C36";
createNode controller -n "biped_lt_toeB_01_loc_tag";
	rename -uid "CAD2C6E4-E44F-C91E-0703-4C8DA699D602";
createNode controller -n "biped_lt_toeB_02_loc_tag";
	rename -uid "CACAB546-994D-82E1-F87A-62ADEA4C41F6";
createNode controller -n "biped_lt_toeB_03_loc_tag";
	rename -uid "2E0E69AD-0F41-A335-C66B-EBB56B3629B7";
createNode controller -n "biped_lt_toeC_01_loc_tag";
	rename -uid "EE29D3C1-3A40-7A27-6BE5-2882BAAEC5CC";
createNode controller -n "biped_lt_toeC_02_loc_tag";
	rename -uid "054699F9-A442-BC3C-98EB-A6A57B8877D3";
createNode controller -n "biped_lt_toeC_03_loc_tag";
	rename -uid "C2715449-6B49-DAE1-2A0D-4CA01D65454E";
createNode controller -n "biped_lt_toeD_01_loc_tag";
	rename -uid "D151AAD6-CA43-98DD-9D28-29B236A6CCE6";
createNode controller -n "biped_lt_toeD_02_loc_tag";
	rename -uid "C3B8DB8E-A743-310B-CC67-39A25459EB45";
createNode controller -n "biped_lt_toeD_03_loc_tag";
	rename -uid "3969E4EE-3E47-3744-3CC9-379137264D02";
createNode controller -n "biped_lt_toeE_01_loc_tag";
	rename -uid "7283FA86-1148-72AC-3415-F090A77FF91B";
createNode controller -n "biped_lt_toeE_02_loc_tag";
	rename -uid "74E228BB-754C-1E7B-E905-E58627003DB7";
createNode controller -n "biped_lt_toeE_03_loc_tag";
	rename -uid "ED3DDF2C-F049-9312-C666-2380E9BF9F13";
createNode controller -n "biped_ct_back_01_loc_tag";
	rename -uid "B8232943-A54B-6CD3-0E63-AE974AD3F33D";
createNode controller -n "biped_ct_back_02_loc_tag";
	rename -uid "F86000B4-9648-6DE8-8DA8-F9B45413BE38";
createNode controller -n "biped_ct_back_03_loc_tag";
	rename -uid "F60B42DE-5945-E662-A1B9-D39A196EA1F6";
createNode controller -n "biped_ct_back_04_loc_tag";
	rename -uid "326FF633-C64C-AA41-E4F4-8B9308A8DB1B";
createNode controller -n "biped_ct_back_05_loc_tag";
	rename -uid "A8E344F8-7040-D3F5-9545-5EB3D359DD7D";
	setAttr -s 2 ".child";
createNode controller -n "biped_ct_back_06_loc_tag";
	rename -uid "B436176D-C343-3120-77F2-BF933C2E6996";
createNode controller -n "biped_ct_back_07_loc_tag";
	rename -uid "6564295F-FC4E-F753-5881-5DA42E9E77E4";
createNode controller -n "biped_ct_neck_01_loc_tag";
	rename -uid "6B07A332-D841-9B82-D6D1-C4B3FF5472A6";
createNode controller -n "biped_ct_neck_02_loc_tag";
	rename -uid "83F7D3B5-EF47-3B0F-B7EA-5B830CB26BAB";
createNode controller -n "biped_ct_neck_03_loc_tag";
	rename -uid "3EC8906D-E445-A4E6-B2AA-12948A4106A1";
createNode controller -n "biped_ct_neck_04_loc_tag";
	rename -uid "65E371DF-7C49-C940-0F11-06A39125DB83";
createNode controller -n "biped_ct_head_01_loc_tag";
	rename -uid "FC301247-394A-937E-B33A-84BA8E658C2F";
	setAttr -s 3 ".child";
createNode controller -n "biped_ct_head_02_loc_tag";
	rename -uid "3C64A021-8E49-190A-8202-CFAB9704EDCD";
createNode controller -n "biped_lt_eye_01_loc_tag";
	rename -uid "16806386-7A4A-04C5-8A98-3199583C0E52";
createNode controller -n "biped_lt_eye_02_loc_tag";
	rename -uid "05795CDE-0345-F45F-59CF-7BB9148A1AEA";
createNode controller -n "biped_ct_jaw_01_loc_tag";
	rename -uid "4F6DB1FC-3D43-966D-1D51-BFB034CE516E";
createNode controller -n "biped_ct_jaw_02_loc_tag";
	rename -uid "315C835E-DB49-5418-856D-0A9A81D6C41B";
createNode controller -n "biped_lt_clav_01_loc_tag";
	rename -uid "94E52DEF-5F45-44BA-7A09-FE8012E18F49";
createNode controller -n "biped_lt_clav_02_loc_tag";
	rename -uid "2148438C-024E-8FF1-0EB7-A18F3672A7BD";
createNode controller -n "biped_lt_arm_01_loc_tag";
	rename -uid "5E11A192-2240-835F-1EB4-46BA1295B546";
createNode controller -n "biped_lt_arm_02_loc_tag";
	rename -uid "16D2AF44-9942-D11C-26AD-CA92FADA2AF6";
createNode controller -n "biped_lt_arm_03_loc_tag";
	rename -uid "018F888C-3649-86D4-84D1-DE84ECA3D99D";
createNode controller -n "biped_lt_hand_01_loc_tag";
	rename -uid "14D2682C-C64C-D05E-C953-9DB8C9A95A2F";
createNode controller -n "biped_lt_hand_02_loc_tag";
	rename -uid "84B4449E-5342-445E-7663-56A873B2C756";
	setAttr -s 5 ".child";
createNode controller -n "biped_lt_thumb_01_pivot_loc_tag";
	rename -uid "A068D7B7-7F49-3A3C-AFB2-43B8E9CE669D";
createNode controller -n "biped_lt_thumb_02_loc_tag";
	rename -uid "A3E31A16-DE4D-D527-7677-FAB0E72FE674";
createNode controller -n "biped_lt_thumb_03_loc_tag";
	rename -uid "AE650C5C-504C-2D82-A325-A4BC6E1FE138";
createNode controller -n "biped_lt_thumb_04_loc_tag";
	rename -uid "884C8B97-5C40-8FDC-B15A-33AB95C6ED8C";
createNode controller -n "biped_lt_thumb_05_loc_tag";
	rename -uid "07926613-B54A-A192-16C4-09BCC842D9B2";
createNode controller -n "biped_lt_middle_01_loc_tag";
	rename -uid "E5ABFC62-E540-526A-BDD8-A5B3571B2352";
createNode controller -n "biped_lt_middle_02_loc_tag";
	rename -uid "18F82C73-9042-DB1B-29B0-958CFFA163BE";
createNode controller -n "biped_lt_middle_03_loc_tag";
	rename -uid "87274BFE-6445-9B60-55DB-DA8E4514EEA2";
createNode controller -n "biped_lt_middle_04_loc_tag";
	rename -uid "DA37D573-7740-F82C-C0BE-06B2A767F124";
createNode controller -n "biped_lt_middle_05_loc_tag";
	rename -uid "587F717A-5C43-540F-D434-0E8AECAA7B92";
createNode controller -n "biped_lt_ring_01_loc_tag";
	rename -uid "8D7212C0-224D-39C7-CF9A-78A7B725B69A";
createNode controller -n "biped_lt_ring_02_loc_tag";
	rename -uid "2C6CAB15-744C-BCDC-F442-C6BE1D595870";
createNode controller -n "biped_lt_ring_03_loc_tag";
	rename -uid "B8FB3393-994D-B5A3-CC37-EEB58009AD2C";
createNode controller -n "biped_lt_ring_04_loc_tag";
	rename -uid "8ABDC6DF-134C-52F6-AED4-519BD35A8A89";
createNode controller -n "biped_lt_ring_05_loc_tag";
	rename -uid "F430F397-6849-3D8D-2CBB-8E9671D557F2";
createNode controller -n "biped_lt_pinky_01_loc_tag";
	rename -uid "439BB459-B344-9134-845F-31ABDF697CB7";
createNode controller -n "biped_lt_pinky_02_loc_tag";
	rename -uid "27F93AFD-1C43-8772-F127-08ACA2AD45DA";
createNode controller -n "biped_lt_pinky_03_loc_tag";
	rename -uid "B88707C8-4A44-31C3-2E85-63A78979A7C2";
createNode controller -n "biped_lt_pinky_04_loc_tag";
	rename -uid "730AA42A-9949-17CF-0C93-6B885D345C61";
createNode controller -n "biped_lt_pinky_05_loc_tag";
	rename -uid "5C55931A-9F42-3910-5ECB-30B6D5FF60E2";
createNode controller -n "biped_lt_index_01_loc_tag";
	rename -uid "A3980218-9B4F-47E7-80D9-AD85AD0BC5ED";
createNode controller -n "biped_lt_index_02_loc_tag";
	rename -uid "E0724B1A-9244-5FE4-4B01-99A2017EBA11";
createNode controller -n "biped_lt_index_03_loc_tag";
	rename -uid "7C328984-4249-B664-5935-91B8C7DBF5B5";
createNode controller -n "biped_lt_index_04_loc_tag";
	rename -uid "3ECF6864-374F-AA6A-AF7E-3186D8DC95A9";
createNode controller -n "biped_lt_index_05_loc_tag";
	rename -uid "1039F357-8543-6FF8-6967-879349F9A362";
createNode controller -n "biped_lt_leg_04_fk_icon_tag";
	rename -uid "2885B32B-7445-426C-DA72-C3866B8572D7";
createNode controller -n "biped_lt_leg_03_fk_icon_tag";
	rename -uid "8273B9D6-994B-D07C-2412-A397C07452F9";
createNode controller -n "biped_lt_leg_02_fk_icon_tag";
	rename -uid "C164F591-C544-D35F-ACC1-7D8C0E0FB0F5";
createNode controller -n "biped_lt_leg_01_fk_icon_tag";
	rename -uid "630A1C66-054D-70AD-AC11-A99E4B0EE022";
createNode controller -n "biped_ct_hip_icon_tag";
	rename -uid "5967B091-5C46-A60F-FDEA-C1B4DCEADBC1";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av ".unw";
	setAttr -k on ".etw";
	setAttr -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -s 3 ".r";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -cb on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -cb on ".imfkey";
	setAttr -k on ".gama";
	setAttr -k on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -cb on ".ep";
	setAttr -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".pff";
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -cb on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -k on ".pram";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr -cb on ".hbl";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off ".ctrs" 256;
	setAttr -av -k off ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "transformGeometry1.og" "fitSkeleton_crvShape.cr";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.ctx" "lt_leg_01_fk_icon.tx";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.cty" "lt_leg_01_fk_icon.ty";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.ctz" "lt_leg_01_fk_icon.tz";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.crx" "lt_leg_01_fk_icon.rx";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.cry" "lt_leg_01_fk_icon.ry";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.crz" "lt_leg_01_fk_icon.rz";
connectAttr "transformGeometry3.og" "lt_leg_01_fk_iconShape.cr";
connectAttr "lt_leg_01_fk_icon.ro" "lt_leg_01_fk_icon_parentConstraint1.cro";
connectAttr "lt_leg_01_fk_icon.pim" "lt_leg_01_fk_icon_parentConstraint1.cpim";
connectAttr "lt_leg_01_fk_icon.rp" "lt_leg_01_fk_icon_parentConstraint1.crp";
connectAttr "lt_leg_01_fk_icon.rpt" "lt_leg_01_fk_icon_parentConstraint1.crt";
connectAttr "lt_leg_01_loc.t" "lt_leg_01_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_01_loc.rp" "lt_leg_01_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_01_loc.rpt" "lt_leg_01_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_01_loc.r" "lt_leg_01_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_01_loc.ro" "lt_leg_01_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_01_loc.s" "lt_leg_01_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_01_loc.pm" "lt_leg_01_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_leg_01_fk_icon_parentConstraint1.w0" "lt_leg_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_leg_02_fk_icon_parentConstraint1.ctx" "lt_leg_02_fk_icon.tx";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.cty" "lt_leg_02_fk_icon.ty";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.ctz" "lt_leg_02_fk_icon.tz";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.crx" "lt_leg_02_fk_icon.rx";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.cry" "lt_leg_02_fk_icon.ry";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.crz" "lt_leg_02_fk_icon.rz";
connectAttr "lt_leg_02_fk_icon.ro" "lt_leg_02_fk_icon_parentConstraint1.cro";
connectAttr "lt_leg_02_fk_icon.pim" "lt_leg_02_fk_icon_parentConstraint1.cpim";
connectAttr "lt_leg_02_fk_icon.rp" "lt_leg_02_fk_icon_parentConstraint1.crp";
connectAttr "lt_leg_02_fk_icon.rpt" "lt_leg_02_fk_icon_parentConstraint1.crt";
connectAttr "lt_leg_02_loc.t" "lt_leg_02_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_02_loc.rp" "lt_leg_02_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_02_loc.rpt" "lt_leg_02_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_02_loc.r" "lt_leg_02_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_02_loc.ro" "lt_leg_02_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_02_loc.s" "lt_leg_02_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_02_loc.pm" "lt_leg_02_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_leg_02_fk_icon_parentConstraint1.w0" "lt_leg_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_leg_03_fk_icon_parentConstraint1.ctx" "lt_leg_03_fk_icon.tx";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.cty" "lt_leg_03_fk_icon.ty";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.ctz" "lt_leg_03_fk_icon.tz";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.crx" "lt_leg_03_fk_icon.rx";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.cry" "lt_leg_03_fk_icon.ry";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.crz" "lt_leg_03_fk_icon.rz";
connectAttr "lt_leg_03_fk_icon.ro" "lt_leg_03_fk_icon_parentConstraint1.cro";
connectAttr "lt_leg_03_fk_icon.pim" "lt_leg_03_fk_icon_parentConstraint1.cpim";
connectAttr "lt_leg_03_fk_icon.rp" "lt_leg_03_fk_icon_parentConstraint1.crp";
connectAttr "lt_leg_03_fk_icon.rpt" "lt_leg_03_fk_icon_parentConstraint1.crt";
connectAttr "lt_leg_03_loc.t" "lt_leg_03_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_03_loc.rp" "lt_leg_03_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_03_loc.rpt" "lt_leg_03_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_03_loc.r" "lt_leg_03_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_03_loc.ro" "lt_leg_03_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_03_loc.s" "lt_leg_03_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_03_loc.pm" "lt_leg_03_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_leg_03_fk_icon_parentConstraint1.w0" "lt_leg_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_leg_04_fk_icon_parentConstraint1.ctx" "lt_leg_04_fk_icon.tx";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.cty" "lt_leg_04_fk_icon.ty";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.ctz" "lt_leg_04_fk_icon.tz";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.crx" "lt_leg_04_fk_icon.rx";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.cry" "lt_leg_04_fk_icon.ry";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.crz" "lt_leg_04_fk_icon.rz";
connectAttr "lt_leg_04_fk_icon.ro" "lt_leg_04_fk_icon_parentConstraint1.cro";
connectAttr "lt_leg_04_fk_icon.pim" "lt_leg_04_fk_icon_parentConstraint1.cpim";
connectAttr "lt_leg_04_fk_icon.rp" "lt_leg_04_fk_icon_parentConstraint1.crp";
connectAttr "lt_leg_04_fk_icon.rpt" "lt_leg_04_fk_icon_parentConstraint1.crt";
connectAttr "lt_leg_04_loc.t" "lt_leg_04_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_04_loc.rp" "lt_leg_04_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_04_loc.rpt" "lt_leg_04_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_04_loc.r" "lt_leg_04_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_04_loc.ro" "lt_leg_04_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_04_loc.s" "lt_leg_04_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_04_loc.pm" "lt_leg_04_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_leg_04_fk_icon_parentConstraint1.w0" "lt_leg_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_eyes_icon_parentConstraint1.ctx" "ct_eyes_icon.tx";
connectAttr "ct_eyes_icon_parentConstraint1.cty" "ct_eyes_icon.ty";
connectAttr "ct_eyes_icon_parentConstraint1.ctz" "ct_eyes_icon.tz";
connectAttr "ct_eyes_icon_parentConstraint1.crx" "ct_eyes_icon.rx";
connectAttr "ct_eyes_icon_parentConstraint1.cry" "ct_eyes_icon.ry";
connectAttr "ct_eyes_icon_parentConstraint1.crz" "ct_eyes_icon.rz";
connectAttr "transformGeometry53.og" "ct_eyes_iconShape.cr";
connectAttr "transformGeometry54.og" "rt_eye_iconShape.cr";
connectAttr "transformGeometry55.og" "lt_eye_iconShape.cr";
connectAttr "ct_eyes_icon.ro" "ct_eyes_icon_parentConstraint1.cro";
connectAttr "ct_eyes_icon.pim" "ct_eyes_icon_parentConstraint1.cpim";
connectAttr "ct_eyes_icon.rp" "ct_eyes_icon_parentConstraint1.crp";
connectAttr "ct_eyes_icon.rpt" "ct_eyes_icon_parentConstraint1.crt";
connectAttr "lt_eye_01_loc.t" "ct_eyes_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_eye_01_loc.rp" "ct_eyes_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_eye_01_loc.rpt" "ct_eyes_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_eye_01_loc.r" "ct_eyes_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_eye_01_loc.ro" "ct_eyes_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_eye_01_loc.s" "ct_eyes_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_eye_01_loc.pm" "ct_eyes_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_eyes_icon_parentConstraint1.w0" "ct_eyes_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_jaw_icon_parentConstraint1.cty" "ct_jaw_icon.ty";
connectAttr "ct_jaw_icon_parentConstraint1.ctz" "ct_jaw_icon.tz";
connectAttr "ct_jaw_icon_parentConstraint1.ctx" "ct_jaw_icon.tx";
connectAttr "ct_jaw_icon_parentConstraint1.crx" "ct_jaw_icon.rx";
connectAttr "ct_jaw_icon_parentConstraint1.cry" "ct_jaw_icon.ry";
connectAttr "ct_jaw_icon_parentConstraint1.crz" "ct_jaw_icon.rz";
connectAttr "ct_jaw_icon.ro" "ct_jaw_icon_parentConstraint1.cro";
connectAttr "ct_jaw_icon.pim" "ct_jaw_icon_parentConstraint1.cpim";
connectAttr "ct_jaw_icon.rp" "ct_jaw_icon_parentConstraint1.crp";
connectAttr "ct_jaw_icon.rpt" "ct_jaw_icon_parentConstraint1.crt";
connectAttr "ct_jaw_01_loc.t" "ct_jaw_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_jaw_01_loc.rp" "ct_jaw_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_jaw_01_loc.rpt" "ct_jaw_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_jaw_01_loc.r" "ct_jaw_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_jaw_01_loc.ro" "ct_jaw_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_jaw_01_loc.s" "ct_jaw_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_jaw_01_loc.pm" "ct_jaw_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_jaw_icon_parentConstraint1.w0" "ct_jaw_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_foot_icon_parentConstraint1.ctx" "lt_foot_icon.tx";
connectAttr "lt_foot_icon_parentConstraint1.cty" "lt_foot_icon.ty";
connectAttr "lt_foot_icon_parentConstraint1.ctz" "lt_foot_icon.tz";
connectAttr "lt_foot_icon_parentConstraint1.crx" "lt_foot_icon.rx";
connectAttr "lt_foot_icon_parentConstraint1.cry" "lt_foot_icon.ry";
connectAttr "lt_foot_icon_parentConstraint1.crz" "lt_foot_icon.rz";
connectAttr "lt_foot_icon.ro" "lt_foot_icon_parentConstraint1.cro";
connectAttr "lt_foot_icon.pim" "lt_foot_icon_parentConstraint1.cpim";
connectAttr "lt_foot_icon.rp" "lt_foot_icon_parentConstraint1.crp";
connectAttr "lt_foot_icon.rpt" "lt_foot_icon_parentConstraint1.crt";
connectAttr "lt_leg_03_loc.t" "lt_foot_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_03_loc.rp" "lt_foot_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_03_loc.rpt" "lt_foot_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_03_loc.r" "lt_foot_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_03_loc.ro" "lt_foot_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_03_loc.s" "lt_foot_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_03_loc.pm" "lt_foot_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_foot_icon_parentConstraint1.w0" "lt_foot_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_hip_icon_parentConstraint1.ctx" "ct_hip_icon.tx";
connectAttr "ct_hip_icon_parentConstraint1.cty" "ct_hip_icon.ty";
connectAttr "ct_hip_icon_parentConstraint1.ctz" "ct_hip_icon.tz";
connectAttr "ct_hip_icon_parentConstraint1.crx" "ct_hip_icon.rx";
connectAttr "ct_hip_icon_parentConstraint1.cry" "ct_hip_icon.ry";
connectAttr "ct_hip_icon_parentConstraint1.crz" "ct_hip_icon.rz";
connectAttr "ct_hip_icon.ro" "ct_hip_icon_parentConstraint1.cro";
connectAttr "ct_hip_icon.pim" "ct_hip_icon_parentConstraint1.cpim";
connectAttr "ct_hip_icon.rp" "ct_hip_icon_parentConstraint1.crp";
connectAttr "ct_hip_icon.rpt" "ct_hip_icon_parentConstraint1.crt";
connectAttr "ct_hip_loc.t" "ct_hip_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_hip_loc.rp" "ct_hip_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_hip_loc.rpt" "ct_hip_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_hip_loc.r" "ct_hip_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_hip_loc.ro" "ct_hip_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_hip_loc.s" "ct_hip_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_hip_loc.pm" "ct_hip_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_hip_icon_parentConstraint1.w0" "ct_hip_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_back_icon_parentConstraint1.ctx" "ct_back_icon.tx";
connectAttr "ct_back_icon_parentConstraint1.cty" "ct_back_icon.ty";
connectAttr "ct_back_icon_parentConstraint1.ctz" "ct_back_icon.tz";
connectAttr "ct_back_icon_parentConstraint1.crx" "ct_back_icon.rx";
connectAttr "ct_back_icon_parentConstraint1.cry" "ct_back_icon.ry";
connectAttr "ct_back_icon_parentConstraint1.crz" "ct_back_icon.rz";
connectAttr "ct_back_icon.ro" "ct_back_icon_parentConstraint1.cro";
connectAttr "ct_back_icon.pim" "ct_back_icon_parentConstraint1.cpim";
connectAttr "ct_back_icon.rp" "ct_back_icon_parentConstraint1.crp";
connectAttr "ct_back_icon.rpt" "ct_back_icon_parentConstraint1.crt";
connectAttr "ct_back_01_loc.t" "ct_back_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_back_01_loc.rp" "ct_back_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_back_01_loc.rpt" "ct_back_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_back_01_loc.r" "ct_back_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_back_01_loc.ro" "ct_back_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_back_01_loc.s" "ct_back_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_back_01_loc.pm" "ct_back_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_back_icon_parentConstraint1.w0" "ct_back_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_COG_icon_parentConstraint1.ctx" "ct_COG_icon.tx";
connectAttr "ct_COG_icon_parentConstraint1.cty" "ct_COG_icon.ty";
connectAttr "ct_COG_icon_parentConstraint1.ctz" "ct_COG_icon.tz";
connectAttr "ct_COG_icon_parentConstraint1.crx" "ct_COG_icon.rx";
connectAttr "ct_COG_icon_parentConstraint1.cry" "ct_COG_icon.ry";
connectAttr "ct_COG_icon_parentConstraint1.crz" "ct_COG_icon.rz";
connectAttr "transformGeometry22.og" "ct_COG_iconShape.cr";
connectAttr "ct_COG_icon.ro" "ct_COG_icon_parentConstraint1.cro";
connectAttr "ct_COG_icon.pim" "ct_COG_icon_parentConstraint1.cpim";
connectAttr "ct_COG_icon.rp" "ct_COG_icon_parentConstraint1.crp";
connectAttr "ct_COG_icon.rpt" "ct_COG_icon_parentConstraint1.crt";
connectAttr "ct_hip_loc.t" "ct_COG_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_hip_loc.rp" "ct_COG_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_hip_loc.rpt" "ct_COG_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_hip_loc.r" "ct_COG_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_hip_loc.ro" "ct_COG_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_hip_loc.s" "ct_COG_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_hip_loc.pm" "ct_COG_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_COG_icon_parentConstraint1.w0" "ct_COG_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_back_01_fk_icon_parentConstraint1.ctx" "ct_back_01_fk_icon.tx";
connectAttr "ct_back_01_fk_icon_parentConstraint1.cty" "ct_back_01_fk_icon.ty";
connectAttr "ct_back_01_fk_icon_parentConstraint1.ctz" "ct_back_01_fk_icon.tz";
connectAttr "ct_back_01_fk_icon_parentConstraint1.crx" "ct_back_01_fk_icon.rx";
connectAttr "ct_back_01_fk_icon_parentConstraint1.cry" "ct_back_01_fk_icon.ry";
connectAttr "ct_back_01_fk_icon_parentConstraint1.crz" "ct_back_01_fk_icon.rz";
connectAttr "transformGeometry69.og" "ct_back_01_fk_iconShape.cr";
connectAttr "ct_back_01_fk_icon.ro" "ct_back_01_fk_icon_parentConstraint1.cro";
connectAttr "ct_back_01_fk_icon.pim" "ct_back_01_fk_icon_parentConstraint1.cpim"
		;
connectAttr "ct_back_01_fk_icon.rp" "ct_back_01_fk_icon_parentConstraint1.crp";
connectAttr "ct_back_01_fk_icon.rpt" "ct_back_01_fk_icon_parentConstraint1.crt";
connectAttr "ct_back_03_loc.t" "ct_back_01_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_back_03_loc.rp" "ct_back_01_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "ct_back_03_loc.rpt" "ct_back_01_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "ct_back_03_loc.r" "ct_back_01_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_back_03_loc.ro" "ct_back_01_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "ct_back_03_loc.s" "ct_back_01_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_back_03_loc.pm" "ct_back_01_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "ct_back_01_fk_icon_parentConstraint1.w0" "ct_back_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_back_02_fk_icon_parentConstraint1.ctx" "ct_back_02_fk_icon.tx";
connectAttr "ct_back_02_fk_icon_parentConstraint1.cty" "ct_back_02_fk_icon.ty";
connectAttr "ct_back_02_fk_icon_parentConstraint1.ctz" "ct_back_02_fk_icon.tz";
connectAttr "ct_back_02_fk_icon_parentConstraint1.crx" "ct_back_02_fk_icon.rx";
connectAttr "ct_back_02_fk_icon_parentConstraint1.cry" "ct_back_02_fk_icon.ry";
connectAttr "ct_back_02_fk_icon_parentConstraint1.crz" "ct_back_02_fk_icon.rz";
connectAttr "ct_back_02_fk_icon.ro" "ct_back_02_fk_icon_parentConstraint1.cro";
connectAttr "ct_back_02_fk_icon.pim" "ct_back_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "ct_back_02_fk_icon.rp" "ct_back_02_fk_icon_parentConstraint1.crp";
connectAttr "ct_back_02_fk_icon.rpt" "ct_back_02_fk_icon_parentConstraint1.crt";
connectAttr "ct_back_05_loc.t" "ct_back_02_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_back_05_loc.rp" "ct_back_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "ct_back_05_loc.rpt" "ct_back_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "ct_back_05_loc.r" "ct_back_02_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_back_05_loc.ro" "ct_back_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "ct_back_05_loc.s" "ct_back_02_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_back_05_loc.pm" "ct_back_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "ct_back_02_fk_icon_parentConstraint1.w0" "ct_back_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_shoulder_icon_parentConstraint1.ctx" "lt_shoulder_icon.tx";
connectAttr "lt_shoulder_icon_parentConstraint1.cty" "lt_shoulder_icon.ty";
connectAttr "lt_shoulder_icon_parentConstraint1.ctz" "lt_shoulder_icon.tz";
connectAttr "lt_shoulder_icon_parentConstraint1.crx" "lt_shoulder_icon.rx";
connectAttr "lt_shoulder_icon_parentConstraint1.cry" "lt_shoulder_icon.ry";
connectAttr "lt_shoulder_icon_parentConstraint1.crz" "lt_shoulder_icon.rz";
connectAttr "lt_shoulder_icon.ro" "lt_shoulder_icon_parentConstraint1.cro";
connectAttr "lt_shoulder_icon.pim" "lt_shoulder_icon_parentConstraint1.cpim";
connectAttr "lt_shoulder_icon.rp" "lt_shoulder_icon_parentConstraint1.crp";
connectAttr "lt_shoulder_icon.rpt" "lt_shoulder_icon_parentConstraint1.crt";
connectAttr "lt_clav_01_loc.t" "lt_shoulder_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_clav_01_loc.rp" "lt_shoulder_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_clav_01_loc.rpt" "lt_shoulder_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_clav_01_loc.r" "lt_shoulder_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_clav_01_loc.ro" "lt_shoulder_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_clav_01_loc.s" "lt_shoulder_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_clav_01_loc.pm" "lt_shoulder_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_shoulder_icon_parentConstraint1.w0" "lt_shoulder_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_chest_icon_parentConstraint1.ctx" "ct_chest_icon.tx";
connectAttr "ct_chest_icon_parentConstraint1.cty" "ct_chest_icon.ty";
connectAttr "ct_chest_icon_parentConstraint1.ctz" "ct_chest_icon.tz";
connectAttr "ct_chest_icon_parentConstraint1.crx" "ct_chest_icon.rx";
connectAttr "ct_chest_icon_parentConstraint1.cry" "ct_chest_icon.ry";
connectAttr "ct_chest_icon_parentConstraint1.crz" "ct_chest_icon.rz";
connectAttr "ct_chest_icon.ro" "ct_chest_icon_parentConstraint1.cro";
connectAttr "ct_chest_icon.pim" "ct_chest_icon_parentConstraint1.cpim";
connectAttr "ct_chest_icon.rp" "ct_chest_icon_parentConstraint1.crp";
connectAttr "ct_chest_icon.rpt" "ct_chest_icon_parentConstraint1.crt";
connectAttr "ct_back_07_loc.t" "ct_chest_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_back_07_loc.rp" "ct_chest_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_back_07_loc.rpt" "ct_chest_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_back_07_loc.r" "ct_chest_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_back_07_loc.ro" "ct_chest_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_back_07_loc.s" "ct_chest_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_back_07_loc.pm" "ct_chest_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_chest_icon_parentConstraint1.w0" "ct_chest_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_arm_icon_parentConstraint1.ctx" "lt_arm_icon.tx";
connectAttr "lt_arm_icon_parentConstraint1.cty" "lt_arm_icon.ty";
connectAttr "lt_arm_icon_parentConstraint1.ctz" "lt_arm_icon.tz";
connectAttr "lt_arm_icon_parentConstraint1.crx" "lt_arm_icon.rx";
connectAttr "lt_arm_icon_parentConstraint1.cry" "lt_arm_icon.ry";
connectAttr "lt_arm_icon_parentConstraint1.crz" "lt_arm_icon.rz";
connectAttr "lt_arm_icon.ro" "lt_arm_icon_parentConstraint1.cro";
connectAttr "lt_arm_icon.pim" "lt_arm_icon_parentConstraint1.cpim";
connectAttr "lt_arm_icon.rp" "lt_arm_icon_parentConstraint1.crp";
connectAttr "lt_arm_icon.rpt" "lt_arm_icon_parentConstraint1.crt";
connectAttr "lt_arm_03_loc.t" "lt_arm_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_arm_03_loc.rp" "lt_arm_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_arm_03_loc.rpt" "lt_arm_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_arm_03_loc.r" "lt_arm_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_arm_03_loc.ro" "lt_arm_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_arm_03_loc.s" "lt_arm_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_arm_03_loc.pm" "lt_arm_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_arm_icon_parentConstraint1.w0" "lt_arm_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_arm_01_fk_icon_parentConstraint1.ctx" "lt_arm_01_fk_icon.tx";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.cty" "lt_arm_01_fk_icon.ty";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.ctz" "lt_arm_01_fk_icon.tz";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.crx" "lt_arm_01_fk_icon.rx";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.cry" "lt_arm_01_fk_icon.ry";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.crz" "lt_arm_01_fk_icon.rz";
connectAttr "transformGeometry26.og" "lt_arm_01_fk_iconShape.cr";
connectAttr "lt_arm_01_fk_icon.ro" "lt_arm_01_fk_icon_parentConstraint1.cro";
connectAttr "lt_arm_01_fk_icon.pim" "lt_arm_01_fk_icon_parentConstraint1.cpim";
connectAttr "lt_arm_01_fk_icon.rp" "lt_arm_01_fk_icon_parentConstraint1.crp";
connectAttr "lt_arm_01_fk_icon.rpt" "lt_arm_01_fk_icon_parentConstraint1.crt";
connectAttr "lt_arm_01_loc.t" "lt_arm_01_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_arm_01_loc.rp" "lt_arm_01_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_arm_01_loc.rpt" "lt_arm_01_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_arm_01_loc.r" "lt_arm_01_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_arm_01_loc.ro" "lt_arm_01_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_arm_01_loc.s" "lt_arm_01_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_arm_01_loc.pm" "lt_arm_01_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_arm_01_fk_icon_parentConstraint1.w0" "lt_arm_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_arm_02_fk_icon_parentConstraint1.ctx" "lt_arm_02_fk_icon.tx";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.cty" "lt_arm_02_fk_icon.ty";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.ctz" "lt_arm_02_fk_icon.tz";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.crx" "lt_arm_02_fk_icon.rx";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.cry" "lt_arm_02_fk_icon.ry";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.crz" "lt_arm_02_fk_icon.rz";
connectAttr "lt_arm_02_fk_icon.ro" "lt_arm_02_fk_icon_parentConstraint1.cro";
connectAttr "lt_arm_02_fk_icon.pim" "lt_arm_02_fk_icon_parentConstraint1.cpim";
connectAttr "lt_arm_02_fk_icon.rp" "lt_arm_02_fk_icon_parentConstraint1.crp";
connectAttr "lt_arm_02_fk_icon.rpt" "lt_arm_02_fk_icon_parentConstraint1.crt";
connectAttr "lt_arm_02_loc.t" "lt_arm_02_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_arm_02_loc.rp" "lt_arm_02_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_arm_02_loc.rpt" "lt_arm_02_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_arm_02_loc.r" "lt_arm_02_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_arm_02_loc.ro" "lt_arm_02_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_arm_02_loc.s" "lt_arm_02_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_arm_02_loc.pm" "lt_arm_02_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_arm_02_fk_icon_parentConstraint1.w0" "lt_arm_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_hand_icon_parentConstraint1.ctx" "lt_hand_icon.tx";
connectAttr "lt_hand_icon_parentConstraint1.cty" "lt_hand_icon.ty";
connectAttr "lt_hand_icon_parentConstraint1.ctz" "lt_hand_icon.tz";
connectAttr "lt_hand_icon_parentConstraint1.crx" "lt_hand_icon.rx";
connectAttr "lt_hand_icon_parentConstraint1.cry" "lt_hand_icon.ry";
connectAttr "lt_hand_icon_parentConstraint1.crz" "lt_hand_icon.rz";
connectAttr "transformGeometry62.og" "lt_hand_iconShape.cr";
connectAttr "lt_hand_icon.ro" "lt_hand_icon_parentConstraint1.cro";
connectAttr "lt_hand_icon.pim" "lt_hand_icon_parentConstraint1.cpim";
connectAttr "lt_hand_icon.rp" "lt_hand_icon_parentConstraint1.crp";
connectAttr "lt_hand_icon.rpt" "lt_hand_icon_parentConstraint1.crt";
connectAttr "lt_hand_01_loc.t" "lt_hand_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_hand_01_loc.rp" "lt_hand_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_hand_01_loc.rpt" "lt_hand_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_hand_01_loc.r" "lt_hand_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_hand_01_loc.ro" "lt_hand_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_hand_01_loc.s" "lt_hand_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_hand_01_loc.pm" "lt_hand_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_hand_icon_parentConstraint1.w0" "lt_hand_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.ctx" "lt_thumb_01_fk_pivot_icon.tx"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.cty" "lt_thumb_01_fk_pivot_icon.ty"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.ctz" "lt_thumb_01_fk_pivot_icon.tz"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.crx" "lt_thumb_01_fk_pivot_icon.rx"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.cry" "lt_thumb_01_fk_pivot_icon.ry"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.crz" "lt_thumb_01_fk_pivot_icon.rz"
		;
connectAttr "transformGeometry31.og" "lt_thumb_01_fk_pivot_iconShape.cr";
connectAttr "lt_thumb_01_fk_pivot_icon.ro" "lt_thumb_01_fk_pivot_icon_parentConstraint1.cro"
		;
connectAttr "lt_thumb_01_fk_pivot_icon.pim" "lt_thumb_01_fk_pivot_icon_parentConstraint1.cpim"
		;
connectAttr "lt_thumb_01_fk_pivot_icon.rp" "lt_thumb_01_fk_pivot_icon_parentConstraint1.crp"
		;
connectAttr "lt_thumb_01_fk_pivot_icon.rpt" "lt_thumb_01_fk_pivot_icon_parentConstraint1.crt"
		;
connectAttr "lt_thumb_01_pivot_loc.t" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_thumb_01_pivot_loc.rp" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_thumb_01_pivot_loc.rpt" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_thumb_01_pivot_loc.r" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_thumb_01_pivot_loc.ro" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_thumb_01_pivot_loc.s" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_thumb_01_pivot_loc.pm" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_thumb_01_fk_pivot_icon_parentConstraint1.w0" "lt_thumb_01_fk_pivot_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.ctx" "lt_thumb_02_fk_icon.tx"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.cty" "lt_thumb_02_fk_icon.ty"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.ctz" "lt_thumb_02_fk_icon.tz"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.crx" "lt_thumb_02_fk_icon.rx"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.cry" "lt_thumb_02_fk_icon.ry"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.crz" "lt_thumb_02_fk_icon.rz"
		;
connectAttr "transformGeometry32.og" "lt_thumb_02_fk_iconShape.cr";
connectAttr "lt_thumb_02_fk_icon.ro" "lt_thumb_02_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_thumb_02_fk_icon.pim" "lt_thumb_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_thumb_02_fk_icon.rp" "lt_thumb_02_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_thumb_02_fk_icon.rpt" "lt_thumb_02_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_thumb_02_loc.t" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_thumb_02_loc.rp" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_thumb_02_loc.rpt" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_thumb_02_loc.r" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_thumb_02_loc.ro" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_thumb_02_loc.s" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_thumb_02_loc.pm" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_thumb_02_fk_icon_parentConstraint1.w0" "lt_thumb_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.ctx" "lt_thumb_03_fk_icon.tx"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.cty" "lt_thumb_03_fk_icon.ty"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.ctz" "lt_thumb_03_fk_icon.tz"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.crx" "lt_thumb_03_fk_icon.rx"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.cry" "lt_thumb_03_fk_icon.ry"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.crz" "lt_thumb_03_fk_icon.rz"
		;
connectAttr "lt_thumb_03_fk_icon.ro" "lt_thumb_03_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_thumb_03_fk_icon.pim" "lt_thumb_03_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_thumb_03_fk_icon.rp" "lt_thumb_03_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_thumb_03_fk_icon.rpt" "lt_thumb_03_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_thumb_03_loc.t" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_thumb_03_loc.rp" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_thumb_03_loc.rpt" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_thumb_03_loc.r" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_thumb_03_loc.ro" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_thumb_03_loc.s" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_thumb_03_loc.pm" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_thumb_03_fk_icon_parentConstraint1.w0" "lt_thumb_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.ctx" "lt_thumb_04_fk_icon.tx"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.cty" "lt_thumb_04_fk_icon.ty"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.ctz" "lt_thumb_04_fk_icon.tz"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.crx" "lt_thumb_04_fk_icon.rx"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.cry" "lt_thumb_04_fk_icon.ry"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.crz" "lt_thumb_04_fk_icon.rz"
		;
connectAttr "lt_thumb_04_fk_icon.ro" "lt_thumb_04_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_thumb_04_fk_icon.pim" "lt_thumb_04_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_thumb_04_fk_icon.rp" "lt_thumb_04_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_thumb_04_fk_icon.rpt" "lt_thumb_04_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_thumb_04_loc.t" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_thumb_04_loc.rp" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_thumb_04_loc.rpt" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_thumb_04_loc.r" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_thumb_04_loc.ro" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_thumb_04_loc.s" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_thumb_04_loc.pm" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_thumb_04_fk_icon_parentConstraint1.w0" "lt_thumb_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.ctx" "lt_index_01_fk_icon.tx"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.cty" "lt_index_01_fk_icon.ty"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.ctz" "lt_index_01_fk_icon.tz"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.crx" "lt_index_01_fk_icon.rx"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.cry" "lt_index_01_fk_icon.ry"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.crz" "lt_index_01_fk_icon.rz"
		;
connectAttr "lt_index_01_fk_icon.ro" "lt_index_01_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_index_01_fk_icon.pim" "lt_index_01_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_index_01_fk_icon.rp" "lt_index_01_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_index_01_fk_icon.rpt" "lt_index_01_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_index_01_loc.t" "lt_index_01_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_index_01_loc.rp" "lt_index_01_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_index_01_loc.rpt" "lt_index_01_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_index_01_loc.r" "lt_index_01_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_index_01_loc.ro" "lt_index_01_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_index_01_loc.s" "lt_index_01_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_index_01_loc.pm" "lt_index_01_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_index_01_fk_icon_parentConstraint1.w0" "lt_index_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.ctx" "lt_index_02_fk_icon.tx"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.cty" "lt_index_02_fk_icon.ty"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.ctz" "lt_index_02_fk_icon.tz"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.crx" "lt_index_02_fk_icon.rx"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.cry" "lt_index_02_fk_icon.ry"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.crz" "lt_index_02_fk_icon.rz"
		;
connectAttr "lt_index_02_fk_icon.ro" "lt_index_02_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_index_02_fk_icon.pim" "lt_index_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_index_02_fk_icon.rp" "lt_index_02_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_index_02_fk_icon.rpt" "lt_index_02_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_index_02_loc.t" "lt_index_02_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_index_02_loc.rp" "lt_index_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_index_02_loc.rpt" "lt_index_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_index_02_loc.r" "lt_index_02_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_index_02_loc.ro" "lt_index_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_index_02_loc.s" "lt_index_02_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_index_02_loc.pm" "lt_index_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_index_02_fk_icon_parentConstraint1.w0" "lt_index_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.ctx" "lt_index_03_fk_icon.tx"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.cty" "lt_index_03_fk_icon.ty"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.ctz" "lt_index_03_fk_icon.tz"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.crx" "lt_index_03_fk_icon.rx"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.cry" "lt_index_03_fk_icon.ry"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.crz" "lt_index_03_fk_icon.rz"
		;
connectAttr "lt_index_03_fk_icon.ro" "lt_index_03_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_index_03_fk_icon.pim" "lt_index_03_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_index_03_fk_icon.rp" "lt_index_03_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_index_03_fk_icon.rpt" "lt_index_03_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_index_03_loc.t" "lt_index_03_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_index_03_loc.rp" "lt_index_03_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_index_03_loc.rpt" "lt_index_03_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_index_03_loc.r" "lt_index_03_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_index_03_loc.ro" "lt_index_03_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_index_03_loc.s" "lt_index_03_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_index_03_loc.pm" "lt_index_03_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_index_03_fk_icon_parentConstraint1.w0" "lt_index_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.ctx" "lt_index_04_fk_icon.tx"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.cty" "lt_index_04_fk_icon.ty"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.ctz" "lt_index_04_fk_icon.tz"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.crx" "lt_index_04_fk_icon.rx"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.cry" "lt_index_04_fk_icon.ry"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.crz" "lt_index_04_fk_icon.rz"
		;
connectAttr "lt_index_04_fk_icon.ro" "lt_index_04_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_index_04_fk_icon.pim" "lt_index_04_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_index_04_fk_icon.rp" "lt_index_04_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_index_04_fk_icon.rpt" "lt_index_04_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_index_04_loc.t" "lt_index_04_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_index_04_loc.rp" "lt_index_04_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_index_04_loc.rpt" "lt_index_04_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_index_04_loc.r" "lt_index_04_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_index_04_loc.ro" "lt_index_04_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_index_04_loc.s" "lt_index_04_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_index_04_loc.pm" "lt_index_04_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_index_04_fk_icon_parentConstraint1.w0" "lt_index_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.ctx" "lt_middle_01_fk_icon.tx"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.cty" "lt_middle_01_fk_icon.ty"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.ctz" "lt_middle_01_fk_icon.tz"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.crx" "lt_middle_01_fk_icon.rx"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.cry" "lt_middle_01_fk_icon.ry"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.crz" "lt_middle_01_fk_icon.rz"
		;
connectAttr "lt_middle_01_fk_icon.ro" "lt_middle_01_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_middle_01_fk_icon.pim" "lt_middle_01_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_middle_01_fk_icon.rp" "lt_middle_01_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_middle_01_fk_icon.rpt" "lt_middle_01_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_middle_01_loc.t" "lt_middle_01_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_middle_01_loc.rp" "lt_middle_01_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_middle_01_loc.rpt" "lt_middle_01_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_middle_01_loc.r" "lt_middle_01_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_middle_01_loc.ro" "lt_middle_01_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_middle_01_loc.s" "lt_middle_01_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_middle_01_loc.pm" "lt_middle_01_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_middle_01_fk_icon_parentConstraint1.w0" "lt_middle_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.ctx" "lt_middle_02_fk_icon.tx"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.cty" "lt_middle_02_fk_icon.ty"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.ctz" "lt_middle_02_fk_icon.tz"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.crx" "lt_middle_02_fk_icon.rx"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.cry" "lt_middle_02_fk_icon.ry"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.crz" "lt_middle_02_fk_icon.rz"
		;
connectAttr "lt_middle_02_fk_icon.ro" "lt_middle_02_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_middle_02_fk_icon.pim" "lt_middle_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_middle_02_fk_icon.rp" "lt_middle_02_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_middle_02_fk_icon.rpt" "lt_middle_02_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_middle_02_loc.t" "lt_middle_02_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_middle_02_loc.rp" "lt_middle_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_middle_02_loc.rpt" "lt_middle_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_middle_02_loc.r" "lt_middle_02_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_middle_02_loc.ro" "lt_middle_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_middle_02_loc.s" "lt_middle_02_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_middle_02_loc.pm" "lt_middle_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_middle_02_fk_icon_parentConstraint1.w0" "lt_middle_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.ctx" "lt_middle_03_fk_icon.tx"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.cty" "lt_middle_03_fk_icon.ty"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.ctz" "lt_middle_03_fk_icon.tz"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.crx" "lt_middle_03_fk_icon.rx"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.cry" "lt_middle_03_fk_icon.ry"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.crz" "lt_middle_03_fk_icon.rz"
		;
connectAttr "lt_middle_03_fk_icon.ro" "lt_middle_03_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_middle_03_fk_icon.pim" "lt_middle_03_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_middle_03_fk_icon.rp" "lt_middle_03_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_middle_03_fk_icon.rpt" "lt_middle_03_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_middle_03_loc.t" "lt_middle_03_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_middle_03_loc.rp" "lt_middle_03_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_middle_03_loc.rpt" "lt_middle_03_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_middle_03_loc.r" "lt_middle_03_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_middle_03_loc.ro" "lt_middle_03_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_middle_03_loc.s" "lt_middle_03_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_middle_03_loc.pm" "lt_middle_03_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_middle_03_fk_icon_parentConstraint1.w0" "lt_middle_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.ctx" "lt_middle_04_fk_icon.tx"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.cty" "lt_middle_04_fk_icon.ty"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.ctz" "lt_middle_04_fk_icon.tz"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.crx" "lt_middle_04_fk_icon.rx"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.cry" "lt_middle_04_fk_icon.ry"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.crz" "lt_middle_04_fk_icon.rz"
		;
connectAttr "lt_middle_04_fk_icon.ro" "lt_middle_04_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_middle_04_fk_icon.pim" "lt_middle_04_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_middle_04_fk_icon.rp" "lt_middle_04_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_middle_04_fk_icon.rpt" "lt_middle_04_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_middle_04_loc.t" "lt_middle_04_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_middle_04_loc.rp" "lt_middle_04_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_middle_04_loc.rpt" "lt_middle_04_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_middle_04_loc.r" "lt_middle_04_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_middle_04_loc.ro" "lt_middle_04_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_middle_04_loc.s" "lt_middle_04_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_middle_04_loc.pm" "lt_middle_04_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_middle_04_fk_icon_parentConstraint1.w0" "lt_middle_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_ring_01_fk_icon_parentConstraint1.ctx" "lt_ring_01_fk_icon.tx";
connectAttr "lt_ring_01_fk_icon_parentConstraint1.cty" "lt_ring_01_fk_icon.ty";
connectAttr "lt_ring_01_fk_icon_parentConstraint1.ctz" "lt_ring_01_fk_icon.tz";
connectAttr "lt_ring_01_fk_icon_parentConstraint1.crx" "lt_ring_01_fk_icon.rx";
connectAttr "lt_ring_01_fk_icon_parentConstraint1.cry" "lt_ring_01_fk_icon.ry";
connectAttr "lt_ring_01_fk_icon_parentConstraint1.crz" "lt_ring_01_fk_icon.rz";
connectAttr "lt_ring_01_fk_icon.ro" "lt_ring_01_fk_icon_parentConstraint1.cro";
connectAttr "lt_ring_01_fk_icon.pim" "lt_ring_01_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_ring_01_fk_icon.rp" "lt_ring_01_fk_icon_parentConstraint1.crp";
connectAttr "lt_ring_01_fk_icon.rpt" "lt_ring_01_fk_icon_parentConstraint1.crt";
connectAttr "lt_ring_01_loc.t" "lt_ring_01_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_ring_01_loc.rp" "lt_ring_01_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_ring_01_loc.rpt" "lt_ring_01_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_ring_01_loc.r" "lt_ring_01_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_ring_01_loc.ro" "lt_ring_01_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_ring_01_loc.s" "lt_ring_01_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_ring_01_loc.pm" "lt_ring_01_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_ring_01_fk_icon_parentConstraint1.w0" "lt_ring_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_ring_02_fk_icon_parentConstraint1.ctx" "lt_ring_02_fk_icon.tx";
connectAttr "lt_ring_02_fk_icon_parentConstraint1.cty" "lt_ring_02_fk_icon.ty";
connectAttr "lt_ring_02_fk_icon_parentConstraint1.ctz" "lt_ring_02_fk_icon.tz";
connectAttr "lt_ring_02_fk_icon_parentConstraint1.crx" "lt_ring_02_fk_icon.rx";
connectAttr "lt_ring_02_fk_icon_parentConstraint1.cry" "lt_ring_02_fk_icon.ry";
connectAttr "lt_ring_02_fk_icon_parentConstraint1.crz" "lt_ring_02_fk_icon.rz";
connectAttr "lt_ring_02_fk_icon.ro" "lt_ring_02_fk_icon_parentConstraint1.cro";
connectAttr "lt_ring_02_fk_icon.pim" "lt_ring_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_ring_02_fk_icon.rp" "lt_ring_02_fk_icon_parentConstraint1.crp";
connectAttr "lt_ring_02_fk_icon.rpt" "lt_ring_02_fk_icon_parentConstraint1.crt";
connectAttr "lt_ring_02_loc.t" "lt_ring_02_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_ring_02_loc.rp" "lt_ring_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_ring_02_loc.rpt" "lt_ring_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_ring_02_loc.r" "lt_ring_02_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_ring_02_loc.ro" "lt_ring_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_ring_02_loc.s" "lt_ring_02_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_ring_02_loc.pm" "lt_ring_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_ring_02_fk_icon_parentConstraint1.w0" "lt_ring_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_ring_03_fk_icon_parentConstraint1.ctx" "lt_ring_03_fk_icon.tx";
connectAttr "lt_ring_03_fk_icon_parentConstraint1.cty" "lt_ring_03_fk_icon.ty";
connectAttr "lt_ring_03_fk_icon_parentConstraint1.ctz" "lt_ring_03_fk_icon.tz";
connectAttr "lt_ring_03_fk_icon_parentConstraint1.crx" "lt_ring_03_fk_icon.rx";
connectAttr "lt_ring_03_fk_icon_parentConstraint1.cry" "lt_ring_03_fk_icon.ry";
connectAttr "lt_ring_03_fk_icon_parentConstraint1.crz" "lt_ring_03_fk_icon.rz";
connectAttr "lt_ring_03_fk_icon.ro" "lt_ring_03_fk_icon_parentConstraint1.cro";
connectAttr "lt_ring_03_fk_icon.pim" "lt_ring_03_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_ring_03_fk_icon.rp" "lt_ring_03_fk_icon_parentConstraint1.crp";
connectAttr "lt_ring_03_fk_icon.rpt" "lt_ring_03_fk_icon_parentConstraint1.crt";
connectAttr "lt_ring_03_loc.t" "lt_ring_03_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_ring_03_loc.rp" "lt_ring_03_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_ring_03_loc.rpt" "lt_ring_03_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_ring_03_loc.r" "lt_ring_03_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_ring_03_loc.ro" "lt_ring_03_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_ring_03_loc.s" "lt_ring_03_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_ring_03_loc.pm" "lt_ring_03_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_ring_03_fk_icon_parentConstraint1.w0" "lt_ring_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_ring_04_fk_icon_parentConstraint1.ctx" "lt_ring_04_fk_icon.tx";
connectAttr "lt_ring_04_fk_icon_parentConstraint1.cty" "lt_ring_04_fk_icon.ty";
connectAttr "lt_ring_04_fk_icon_parentConstraint1.ctz" "lt_ring_04_fk_icon.tz";
connectAttr "lt_ring_04_fk_icon_parentConstraint1.crx" "lt_ring_04_fk_icon.rx";
connectAttr "lt_ring_04_fk_icon_parentConstraint1.cry" "lt_ring_04_fk_icon.ry";
connectAttr "lt_ring_04_fk_icon_parentConstraint1.crz" "lt_ring_04_fk_icon.rz";
connectAttr "lt_ring_04_fk_icon.ro" "lt_ring_04_fk_icon_parentConstraint1.cro";
connectAttr "lt_ring_04_fk_icon.pim" "lt_ring_04_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_ring_04_fk_icon.rp" "lt_ring_04_fk_icon_parentConstraint1.crp";
connectAttr "lt_ring_04_fk_icon.rpt" "lt_ring_04_fk_icon_parentConstraint1.crt";
connectAttr "lt_ring_04_loc.t" "lt_ring_04_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_ring_04_loc.rp" "lt_ring_04_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_ring_04_loc.rpt" "lt_ring_04_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_ring_04_loc.r" "lt_ring_04_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_ring_04_loc.ro" "lt_ring_04_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_ring_04_loc.s" "lt_ring_04_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_ring_04_loc.pm" "lt_ring_04_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_ring_04_fk_icon_parentConstraint1.w0" "lt_ring_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.ctx" "lt_pinky_01_fk_icon.tx"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.cty" "lt_pinky_01_fk_icon.ty"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.ctz" "lt_pinky_01_fk_icon.tz"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.crx" "lt_pinky_01_fk_icon.rx"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.cry" "lt_pinky_01_fk_icon.ry"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.crz" "lt_pinky_01_fk_icon.rz"
		;
connectAttr "lt_pinky_01_fk_icon.ro" "lt_pinky_01_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_pinky_01_fk_icon.pim" "lt_pinky_01_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_pinky_01_fk_icon.rp" "lt_pinky_01_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_pinky_01_fk_icon.rpt" "lt_pinky_01_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_pinky_01_loc.t" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_pinky_01_loc.rp" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_pinky_01_loc.rpt" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_pinky_01_loc.r" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_pinky_01_loc.ro" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_pinky_01_loc.s" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_pinky_01_loc.pm" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_pinky_01_fk_icon_parentConstraint1.w0" "lt_pinky_01_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.ctx" "lt_pinky_02_fk_icon.tx"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.cty" "lt_pinky_02_fk_icon.ty"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.ctz" "lt_pinky_02_fk_icon.tz"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.crx" "lt_pinky_02_fk_icon.rx"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.cry" "lt_pinky_02_fk_icon.ry"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.crz" "lt_pinky_02_fk_icon.rz"
		;
connectAttr "lt_pinky_02_fk_icon.ro" "lt_pinky_02_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_pinky_02_fk_icon.pim" "lt_pinky_02_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_pinky_02_fk_icon.rp" "lt_pinky_02_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_pinky_02_fk_icon.rpt" "lt_pinky_02_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_pinky_02_loc.t" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_pinky_02_loc.rp" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_pinky_02_loc.rpt" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_pinky_02_loc.r" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_pinky_02_loc.ro" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_pinky_02_loc.s" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_pinky_02_loc.pm" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_pinky_02_fk_icon_parentConstraint1.w0" "lt_pinky_02_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.ctx" "lt_pinky_03_fk_icon.tx"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.cty" "lt_pinky_03_fk_icon.ty"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.ctz" "lt_pinky_03_fk_icon.tz"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.crx" "lt_pinky_03_fk_icon.rx"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.cry" "lt_pinky_03_fk_icon.ry"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.crz" "lt_pinky_03_fk_icon.rz"
		;
connectAttr "lt_pinky_03_fk_icon.ro" "lt_pinky_03_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_pinky_03_fk_icon.pim" "lt_pinky_03_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_pinky_03_fk_icon.rp" "lt_pinky_03_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_pinky_03_fk_icon.rpt" "lt_pinky_03_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_pinky_03_loc.t" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_pinky_03_loc.rp" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_pinky_03_loc.rpt" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_pinky_03_loc.r" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_pinky_03_loc.ro" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_pinky_03_loc.s" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_pinky_03_loc.pm" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_pinky_03_fk_icon_parentConstraint1.w0" "lt_pinky_03_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.ctx" "lt_pinky_04_fk_icon.tx"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.cty" "lt_pinky_04_fk_icon.ty"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.ctz" "lt_pinky_04_fk_icon.tz"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.crx" "lt_pinky_04_fk_icon.rx"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.cry" "lt_pinky_04_fk_icon.ry"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.crz" "lt_pinky_04_fk_icon.rz"
		;
connectAttr "lt_pinky_04_fk_icon.ro" "lt_pinky_04_fk_icon_parentConstraint1.cro"
		;
connectAttr "lt_pinky_04_fk_icon.pim" "lt_pinky_04_fk_icon_parentConstraint1.cpim"
		;
connectAttr "lt_pinky_04_fk_icon.rp" "lt_pinky_04_fk_icon_parentConstraint1.crp"
		;
connectAttr "lt_pinky_04_fk_icon.rpt" "lt_pinky_04_fk_icon_parentConstraint1.crt"
		;
connectAttr "lt_pinky_04_loc.t" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].tt"
		;
connectAttr "lt_pinky_04_loc.rp" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].trp"
		;
connectAttr "lt_pinky_04_loc.rpt" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_pinky_04_loc.r" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].tr"
		;
connectAttr "lt_pinky_04_loc.ro" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].tro"
		;
connectAttr "lt_pinky_04_loc.s" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].ts"
		;
connectAttr "lt_pinky_04_loc.pm" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].tpm"
		;
connectAttr "lt_pinky_04_fk_icon_parentConstraint1.w0" "lt_pinky_04_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_neck_fk_icon_parentConstraint1.ctx" "ct_neck_fk_icon.tx";
connectAttr "ct_neck_fk_icon_parentConstraint1.cty" "ct_neck_fk_icon.ty";
connectAttr "ct_neck_fk_icon_parentConstraint1.ctz" "ct_neck_fk_icon.tz";
connectAttr "ct_neck_fk_icon_parentConstraint1.crx" "ct_neck_fk_icon.rx";
connectAttr "ct_neck_fk_icon_parentConstraint1.cry" "ct_neck_fk_icon.ry";
connectAttr "ct_neck_fk_icon_parentConstraint1.crz" "ct_neck_fk_icon.rz";
connectAttr "transformGeometry34.og" "ct_neck_fk_iconShape.cr";
connectAttr "ct_neck_fk_icon.ro" "ct_neck_fk_icon_parentConstraint1.cro";
connectAttr "ct_neck_fk_icon.pim" "ct_neck_fk_icon_parentConstraint1.cpim";
connectAttr "ct_neck_fk_icon.rp" "ct_neck_fk_icon_parentConstraint1.crp";
connectAttr "ct_neck_fk_icon.rpt" "ct_neck_fk_icon_parentConstraint1.crt";
connectAttr "ct_neck_01_loc.t" "ct_neck_fk_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_neck_01_loc.rp" "ct_neck_fk_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_neck_01_loc.rpt" "ct_neck_fk_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_neck_01_loc.r" "ct_neck_fk_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_neck_01_loc.ro" "ct_neck_fk_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_neck_01_loc.s" "ct_neck_fk_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_neck_01_loc.pm" "ct_neck_fk_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_neck_fk_icon_parentConstraint1.w0" "ct_neck_fk_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "ct_neck_icon_parentConstraint1.ctx" "ct_neck_icon.tx";
connectAttr "ct_neck_icon_parentConstraint1.cty" "ct_neck_icon.ty";
connectAttr "ct_neck_icon_parentConstraint1.ctz" "ct_neck_icon.tz";
connectAttr "ct_neck_icon_parentConstraint1.crx" "ct_neck_icon.rx";
connectAttr "ct_neck_icon_parentConstraint1.cry" "ct_neck_icon.ry";
connectAttr "ct_neck_icon_parentConstraint1.crz" "ct_neck_icon.rz";
connectAttr "ct_neck_icon.ro" "ct_neck_icon_parentConstraint1.cro";
connectAttr "ct_neck_icon.pim" "ct_neck_icon_parentConstraint1.cpim";
connectAttr "ct_neck_icon.rp" "ct_neck_icon_parentConstraint1.crp";
connectAttr "ct_neck_icon.rpt" "ct_neck_icon_parentConstraint1.crt";
connectAttr "ct_neck_04_loc.t" "ct_neck_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_neck_04_loc.rp" "ct_neck_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_neck_04_loc.rpt" "ct_neck_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_neck_04_loc.r" "ct_neck_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_neck_04_loc.ro" "ct_neck_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_neck_04_loc.s" "ct_neck_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_neck_04_loc.pm" "ct_neck_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_neck_icon_parentConstraint1.w0" "ct_neck_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.ctx" "lt_leg_ikfk_switch_icon.tx"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.cty" "lt_leg_ikfk_switch_icon.ty"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.ctz" "lt_leg_ikfk_switch_icon.tz"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.crx" "lt_leg_ikfk_switch_icon.rx"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.cry" "lt_leg_ikfk_switch_icon.ry"
		;
connectAttr "lt_leg_ikfk_switch_parentConstraint1.crz" "lt_leg_ikfk_switch_icon.rz"
		;
connectAttr "transformGeometry36.og" "|fitSkeleton_crv|icon_grp|lt_leg_ikfk_switch_icon|nurbsCircleShape1.cr"
		;
connectAttr "lt_leg_ikfk_switch_icon.ro" "lt_leg_ikfk_switch_parentConstraint1.cro"
		;
connectAttr "lt_leg_ikfk_switch_icon.pim" "lt_leg_ikfk_switch_parentConstraint1.cpim"
		;
connectAttr "lt_leg_ikfk_switch_icon.rp" "lt_leg_ikfk_switch_parentConstraint1.crp"
		;
connectAttr "lt_leg_ikfk_switch_icon.rpt" "lt_leg_ikfk_switch_parentConstraint1.crt"
		;
connectAttr "lt_leg_03_loc.t" "lt_leg_ikfk_switch_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_03_loc.rp" "lt_leg_ikfk_switch_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_03_loc.rpt" "lt_leg_ikfk_switch_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_leg_03_loc.r" "lt_leg_ikfk_switch_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_03_loc.ro" "lt_leg_ikfk_switch_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_03_loc.s" "lt_leg_ikfk_switch_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_03_loc.pm" "lt_leg_ikfk_switch_parentConstraint1.tg[0].tpm";
connectAttr "lt_leg_ikfk_switch_parentConstraint1.w0" "lt_leg_ikfk_switch_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_elbow_icon_pointConstraint1.ctx" "lt_elbow_icon.tx";
connectAttr "lt_elbow_icon_pointConstraint1.cty" "lt_elbow_icon.ty";
connectAttr "lt_elbow_icon_pointConstraint1.ctz" "lt_elbow_icon.tz";
connectAttr "lt_arm_hybrid_icon_orientConstraint1.crx" "lt_arm_hybrid_icon.rx";
connectAttr "lt_arm_hybrid_icon_orientConstraint1.cry" "lt_arm_hybrid_icon.ry";
connectAttr "lt_arm_hybrid_icon_orientConstraint1.crz" "lt_arm_hybrid_icon.rz";
connectAttr "lt_elbow_icon.pim" "lt_elbow_icon_pointConstraint1.cpim";
connectAttr "lt_elbow_icon.rp" "lt_elbow_icon_pointConstraint1.crp";
connectAttr "lt_elbow_icon.rpt" "lt_elbow_icon_pointConstraint1.crt";
connectAttr "lt_arm_02_loc.t" "lt_elbow_icon_pointConstraint1.tg[0].tt";
connectAttr "lt_arm_02_loc.rp" "lt_elbow_icon_pointConstraint1.tg[0].trp";
connectAttr "lt_arm_02_loc.rpt" "lt_elbow_icon_pointConstraint1.tg[0].trt";
connectAttr "lt_arm_02_loc.pm" "lt_elbow_icon_pointConstraint1.tg[0].tpm";
connectAttr "lt_elbow_icon_pointConstraint1.w0" "lt_elbow_icon_pointConstraint1.tg[0].tw"
		;
connectAttr "lt_knee_icon_parentConstraint1.ctx" "lt_knee_icon.tx";
connectAttr "lt_knee_icon_parentConstraint1.cty" "lt_knee_icon.ty";
connectAttr "lt_knee_icon_parentConstraint1.ctz" "lt_knee_icon.tz";
connectAttr "lt_knee_icon_parentConstraint1.crx" "lt_knee_icon.rx";
connectAttr "lt_knee_icon_parentConstraint1.cry" "lt_knee_icon.ry";
connectAttr "lt_knee_icon_parentConstraint1.crz" "lt_knee_icon.rz";
connectAttr "lt_knee_icon.ro" "lt_knee_icon_parentConstraint1.cro";
connectAttr "lt_knee_icon.pim" "lt_knee_icon_parentConstraint1.cpim";
connectAttr "lt_knee_icon.rp" "lt_knee_icon_parentConstraint1.crp";
connectAttr "lt_knee_icon.rpt" "lt_knee_icon_parentConstraint1.crt";
connectAttr "lt_leg_02_loc.t" "lt_knee_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_leg_02_loc.rp" "lt_knee_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_leg_02_loc.rpt" "lt_knee_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_leg_02_loc.r" "lt_knee_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_leg_02_loc.ro" "lt_knee_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_leg_02_loc.s" "lt_knee_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_leg_02_loc.pm" "lt_knee_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_knee_icon_parentConstraint1.w0" "lt_knee_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.ctx" "lt_arm_ikfk_switch_icon.tx"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.cty" "lt_arm_ikfk_switch_icon.ty"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.ctz" "lt_arm_ikfk_switch_icon.tz"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.crx" "lt_arm_ikfk_switch_icon.rx"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.cry" "lt_arm_ikfk_switch_icon.ry"
		;
connectAttr "lt_arm_ikfk_switch_parentConstraint1.crz" "lt_arm_ikfk_switch_icon.rz"
		;
connectAttr "lt_arm_ikfk_switch_icon.ro" "lt_arm_ikfk_switch_parentConstraint1.cro"
		;
connectAttr "lt_arm_ikfk_switch_icon.pim" "lt_arm_ikfk_switch_parentConstraint1.cpim"
		;
connectAttr "lt_arm_ikfk_switch_icon.rp" "lt_arm_ikfk_switch_parentConstraint1.crp"
		;
connectAttr "lt_arm_ikfk_switch_icon.rpt" "lt_arm_ikfk_switch_parentConstraint1.crt"
		;
connectAttr "lt_arm_03_loc.t" "lt_arm_ikfk_switch_parentConstraint1.tg[0].tt";
connectAttr "lt_arm_03_loc.rp" "lt_arm_ikfk_switch_parentConstraint1.tg[0].trp";
connectAttr "lt_arm_03_loc.rpt" "lt_arm_ikfk_switch_parentConstraint1.tg[0].trt"
		;
connectAttr "lt_arm_03_loc.r" "lt_arm_ikfk_switch_parentConstraint1.tg[0].tr";
connectAttr "lt_arm_03_loc.ro" "lt_arm_ikfk_switch_parentConstraint1.tg[0].tro";
connectAttr "lt_arm_03_loc.s" "lt_arm_ikfk_switch_parentConstraint1.tg[0].ts";
connectAttr "lt_arm_03_loc.pm" "lt_arm_ikfk_switch_parentConstraint1.tg[0].tpm";
connectAttr "lt_arm_ikfk_switch_parentConstraint1.w0" "lt_arm_ikfk_switch_parentConstraint1.tg[0].tw"
		;
connectAttr "makeNurbCircle21.oc" "moveAll_shape.cr";
connectAttr "makeNurbCircle22.oc" "ct_animShape.cr";
connectAttr "ct_head_icon_parentConstraint1.cty" "ct_head_icon.ty";
connectAttr "ct_head_icon_parentConstraint1.ctz" "ct_head_icon.tz";
connectAttr "ct_head_icon_parentConstraint1.ctx" "ct_head_icon.tx";
connectAttr "ct_head_icon_parentConstraint1.crx" "ct_head_icon.rx";
connectAttr "ct_head_icon_parentConstraint1.cry" "ct_head_icon.ry";
connectAttr "ct_head_icon_parentConstraint1.crz" "ct_head_icon.rz";
connectAttr "transformGeometry56.og" "ct_head_iconShape.cr";
connectAttr "ct_head_icon.ro" "ct_head_icon_parentConstraint1.cro";
connectAttr "ct_head_icon.pim" "ct_head_icon_parentConstraint1.cpim";
connectAttr "ct_head_icon.rp" "ct_head_icon_parentConstraint1.crp";
connectAttr "ct_head_icon.rpt" "ct_head_icon_parentConstraint1.crt";
connectAttr "ct_head_01_loc.t" "ct_head_icon_parentConstraint1.tg[0].tt";
connectAttr "ct_head_01_loc.rp" "ct_head_icon_parentConstraint1.tg[0].trp";
connectAttr "ct_head_01_loc.rpt" "ct_head_icon_parentConstraint1.tg[0].trt";
connectAttr "ct_head_01_loc.r" "ct_head_icon_parentConstraint1.tg[0].tr";
connectAttr "ct_head_01_loc.ro" "ct_head_icon_parentConstraint1.tg[0].tro";
connectAttr "ct_head_01_loc.s" "ct_head_icon_parentConstraint1.tg[0].ts";
connectAttr "ct_head_01_loc.pm" "ct_head_icon_parentConstraint1.tg[0].tpm";
connectAttr "ct_head_icon_parentConstraint1.w0" "ct_head_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_fingers_icon_parentConstraint1.ctx" "lt_fingers_icon.tx";
connectAttr "lt_fingers_icon_parentConstraint1.cty" "lt_fingers_icon.ty";
connectAttr "lt_fingers_icon_parentConstraint1.ctz" "lt_fingers_icon.tz";
connectAttr "lt_fingers_icon_parentConstraint1.crx" "lt_fingers_icon.rx";
connectAttr "lt_fingers_icon_parentConstraint1.cry" "lt_fingers_icon.ry";
connectAttr "lt_fingers_icon_parentConstraint1.crz" "lt_fingers_icon.rz";
connectAttr "transformGeometry63.og" "lt_fingers_iconShape.cr";
connectAttr "transformGeometry64.og" "lt_index_ik_iconShape.cr";
connectAttr "transformGeometry65.og" "lt_middle_ik_iconShape.cr";
connectAttr "transformGeometry66.og" "lt_ring_ik_iconShape.cr";
connectAttr "transformGeometry67.og" "lt_pinky_ik_iconShape.cr";
connectAttr "lt_fingers_icon.ro" "lt_fingers_icon_parentConstraint1.cro";
connectAttr "lt_fingers_icon.pim" "lt_fingers_icon_parentConstraint1.cpim";
connectAttr "lt_fingers_icon.rp" "lt_fingers_icon_parentConstraint1.crp";
connectAttr "lt_fingers_icon.rpt" "lt_fingers_icon_parentConstraint1.crt";
connectAttr "lt_hand_01_loc.t" "lt_fingers_icon_parentConstraint1.tg[0].tt";
connectAttr "lt_hand_01_loc.rp" "lt_fingers_icon_parentConstraint1.tg[0].trp";
connectAttr "lt_hand_01_loc.rpt" "lt_fingers_icon_parentConstraint1.tg[0].trt";
connectAttr "lt_hand_01_loc.r" "lt_fingers_icon_parentConstraint1.tg[0].tr";
connectAttr "lt_hand_01_loc.ro" "lt_fingers_icon_parentConstraint1.tg[0].tro";
connectAttr "lt_hand_01_loc.s" "lt_fingers_icon_parentConstraint1.tg[0].ts";
connectAttr "lt_hand_01_loc.pm" "lt_fingers_icon_parentConstraint1.tg[0].tpm";
connectAttr "lt_fingers_icon_parentConstraint1.w0" "lt_fingers_icon_parentConstraint1.tg[0].tw"
		;
connectAttr "lt_arm_hybrid_icon.ro" "lt_arm_hybrid_icon_orientConstraint1.cro";
connectAttr "lt_arm_hybrid_icon.pim" "lt_arm_hybrid_icon_orientConstraint1.cpim"
		;
connectAttr "lt_arm_02_loc.r" "lt_arm_hybrid_icon_orientConstraint1.tg[0].tr";
connectAttr "lt_arm_02_loc.ro" "lt_arm_hybrid_icon_orientConstraint1.tg[0].tro";
connectAttr "lt_arm_02_loc.pm" "lt_arm_hybrid_icon_orientConstraint1.tg[0].tpm";
connectAttr "lt_arm_hybrid_icon_orientConstraint1.w0" "lt_arm_hybrid_icon_orientConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr ":PxrPathTracer.msg" ":rmanGlobals.ri_integrator";
connectAttr "makeNurbCircle1.oc" "transformGeometry1.ig";
connectAttr "makeNurbCircle2.oc" "transformGeometry2.ig";
connectAttr "transformGeometry2.og" "transformGeometry3.ig";
connectAttr "makeNurbCircle4.oc" "transformGeometry6.ig";
connectAttr "makeNurbCircle6.oc" "transformGeometry7.ig";
connectAttr "makeNurbCircle5.oc" "transformGeometry8.ig";
connectAttr "transformGeometry6.og" "transformGeometry9.ig";
connectAttr "transformGeometry7.og" "transformGeometry10.ig";
connectAttr "transformGeometry8.og" "transformGeometry11.ig";
connectAttr "transformGeometry10.og" "transformGeometry12.ig";
connectAttr "transformGeometry11.og" "transformGeometry13.ig";
connectAttr "transformGeometry9.og" "transformGeometry14.ig";
connectAttr "transformGeometry12.og" "transformGeometry15.ig";
connectAttr "transformGeometry13.og" "transformGeometry16.ig";
connectAttr "makeNurbCircle7.oc" "transformGeometry17.ig";
connectAttr "transformGeometry17.og" "transformGeometry18.ig";
connectAttr "transformGeometry14.og" "transformGeometry19.ig";
connectAttr "transformGeometry15.og" "transformGeometry20.ig";
connectAttr "transformGeometry16.og" "transformGeometry21.ig";
connectAttr "lt_leg_01_loc_tag.pare" "ct_hip_loc_tag.child[0]";
connectAttr "ct_back_01_loc_tag.pare" "ct_hip_loc_tag.child[1]";
connectAttr "lt_leg_02_loc_tag.pare" "lt_leg_01_loc_tag.child[0]";
connectAttr "ct_hip_loc_tag.prep" "lt_leg_01_loc_tag.prep";
connectAttr "lt_leg_03_loc_tag.pare" "lt_leg_02_loc_tag.child[0]";
connectAttr "lt_leg_01_loc_tag.prep" "lt_leg_02_loc_tag.prep";
connectAttr "lt_leg_04_loc_tag.pare" "lt_leg_03_loc_tag.child[0]";
connectAttr "lt_leg_02_loc_tag.prep" "lt_leg_03_loc_tag.prep";
connectAttr "lt_toeA_01_loc_tag.pare" "lt_leg_04_loc_tag.child[0]";
connectAttr "lt_toeB_01_loc_tag.pare" "lt_leg_04_loc_tag.child[1]";
connectAttr "lt_toeC_01_loc_tag.pare" "lt_leg_04_loc_tag.child[2]";
connectAttr "lt_toeD_01_loc_tag.pare" "lt_leg_04_loc_tag.child[3]";
connectAttr "lt_toeE_01_loc_tag.pare" "lt_leg_04_loc_tag.child[4]";
connectAttr "lt_leg_03_loc_tag.prep" "lt_leg_04_loc_tag.prep";
connectAttr "lt_toeA_02_loc_tag.pare" "lt_toeA_01_loc_tag.child[0]";
connectAttr "lt_leg_04_loc_tag.prep" "lt_toeA_01_loc_tag.prep";
connectAttr "lt_toeA_03_loc_tag.pare" "lt_toeA_02_loc_tag.child[0]";
connectAttr "lt_toeA_01_loc_tag.prep" "lt_toeA_02_loc_tag.prep";
connectAttr "lt_toeA_02_loc_tag.prep" "lt_toeA_03_loc_tag.prep";
connectAttr "lt_toeB_02_loc_tag.pare" "lt_toeB_01_loc_tag.child[0]";
connectAttr "lt_leg_04_loc_tag.prep" "lt_toeB_01_loc_tag.prep";
connectAttr "lt_toeB_03_loc_tag.pare" "lt_toeB_02_loc_tag.child[0]";
connectAttr "lt_toeB_01_loc_tag.prep" "lt_toeB_02_loc_tag.prep";
connectAttr "lt_toeB_02_loc_tag.prep" "lt_toeB_03_loc_tag.prep";
connectAttr "lt_toeC_02_loc_tag.pare" "lt_toeC_01_loc_tag.child[0]";
connectAttr "lt_leg_04_loc_tag.prep" "lt_toeC_01_loc_tag.prep";
connectAttr "lt_toeC_03_loc_tag.pare" "lt_toeC_02_loc_tag.child[0]";
connectAttr "lt_toeC_01_loc_tag.prep" "lt_toeC_02_loc_tag.prep";
connectAttr "lt_toeC_02_loc_tag.prep" "lt_toeC_03_loc_tag.prep";
connectAttr "lt_toeD_02_loc_tag.pare" "lt_toeD_01_loc_tag.child[0]";
connectAttr "lt_leg_04_loc_tag.prep" "lt_toeD_01_loc_tag.prep";
connectAttr "lt_toeD_03_loc_tag.pare" "lt_toeD_02_loc_tag.child[0]";
connectAttr "lt_toeD_01_loc_tag.prep" "lt_toeD_02_loc_tag.prep";
connectAttr "lt_toeD_02_loc_tag.prep" "lt_toeD_03_loc_tag.prep";
connectAttr "lt_toeE_02_loc_tag.pare" "lt_toeE_01_loc_tag.child[0]";
connectAttr "lt_leg_04_loc_tag.prep" "lt_toeE_01_loc_tag.prep";
connectAttr "lt_toeE_03_loc_tag.pare" "lt_toeE_02_loc_tag.child[0]";
connectAttr "lt_toeE_01_loc_tag.prep" "lt_toeE_02_loc_tag.prep";
connectAttr "lt_toeE_02_loc_tag.prep" "lt_toeE_03_loc_tag.prep";
connectAttr "ct_hip_loc_tag.prep" "ct_back_01_loc_tag.prep";
connectAttr "ct_back_02_loc_tag.pare" "ct_back_01_loc_tag.child[0]";
connectAttr "ct_back_01_loc_tag.prep" "ct_back_02_loc_tag.prep";
connectAttr "ct_back_03_loc_tag.pare" "ct_back_02_loc_tag.child[0]";
connectAttr "ct_back_02_loc_tag.prep" "ct_back_03_loc_tag.prep";
connectAttr "ct_back_04_loc_tag.pare" "ct_back_03_loc_tag.child[0]";
connectAttr "ct_back_03_loc_tag.prep" "ct_back_04_loc_tag.prep";
connectAttr "ct_back_05_loc_tag.pare" "ct_back_04_loc_tag.child[0]";
connectAttr "ct_back_04_loc_tag.prep" "ct_back_05_loc_tag.prep";
connectAttr "ct_back_06_loc_tag.pare" "ct_back_05_loc_tag.child[0]";
connectAttr "lt_clav_01_loc_tag.pare" "ct_back_05_loc_tag.child[1]";
connectAttr "ct_back_05_loc_tag.prep" "ct_back_06_loc_tag.prep";
connectAttr "ct_back_07_loc_tag.pare" "ct_back_06_loc_tag.child[0]";
connectAttr "ct_back_06_loc_tag.prep" "ct_back_07_loc_tag.prep";
connectAttr "ct_neck_01_loc_tag.pare" "ct_back_07_loc_tag.child[0]";
connectAttr "ct_back_07_loc_tag.prep" "ct_neck_01_loc_tag.prep";
connectAttr "ct_neck_02_loc_tag.pare" "ct_neck_01_loc_tag.child[0]";
connectAttr "ct_neck_01_loc_tag.prep" "ct_neck_02_loc_tag.prep";
connectAttr "ct_neck_03_loc_tag.pare" "ct_neck_02_loc_tag.child[0]";
connectAttr "ct_neck_02_loc_tag.prep" "ct_neck_03_loc_tag.prep";
connectAttr "ct_neck_04_loc_tag.pare" "ct_neck_03_loc_tag.child[0]";
connectAttr "ct_neck_03_loc_tag.prep" "ct_neck_04_loc_tag.prep";
connectAttr "ct_head_01_loc_tag.pare" "ct_neck_04_loc_tag.child[0]";
connectAttr "ct_neck_04_loc_tag.prep" "ct_head_01_loc_tag.prep";
connectAttr "ct_head_02_loc_tag.pare" "ct_head_01_loc_tag.child[0]";
connectAttr "ct_jaw_01_loc_tag.pare" "ct_head_01_loc_tag.child[1]";
connectAttr "lt_eye_01_loc_tag.pare" "ct_head_01_loc_tag.child[2]";
connectAttr "ct_head_01_loc_tag.prep" "ct_head_02_loc_tag.prep";
connectAttr "ct_head_01_loc_tag.prep" "lt_eye_01_loc_tag.prep";
connectAttr "lt_eye_02_loc_tag.pare" "lt_eye_01_loc_tag.child[0]";
connectAttr "lt_eye_01_loc_tag.prep" "lt_eye_02_loc_tag.prep";
connectAttr "ct_head_01_loc_tag.prep" "ct_jaw_01_loc_tag.prep";
connectAttr "ct_jaw_02_loc_tag.pare" "ct_jaw_01_loc_tag.child[0]";
connectAttr "ct_jaw_01_loc_tag.prep" "ct_jaw_02_loc_tag.prep";
connectAttr "ct_back_05_loc_tag.prep" "lt_clav_01_loc_tag.prep";
connectAttr "lt_clav_02_loc_tag.pare" "lt_clav_01_loc_tag.child[0]";
connectAttr "lt_clav_01_loc_tag.prep" "lt_clav_02_loc_tag.prep";
connectAttr "lt_arm_01_loc_tag.pare" "lt_clav_02_loc_tag.child[0]";
connectAttr "lt_clav_02_loc_tag.prep" "lt_arm_01_loc_tag.prep";
connectAttr "lt_arm_02_loc_tag.pare" "lt_arm_01_loc_tag.child[0]";
connectAttr "lt_arm_01_loc_tag.prep" "lt_arm_02_loc_tag.prep";
connectAttr "lt_arm_03_loc_tag.pare" "lt_arm_02_loc_tag.child[0]";
connectAttr "lt_arm_02_loc_tag.prep" "lt_arm_03_loc_tag.prep";
connectAttr "lt_hand_01_loc_tag.pare" "lt_arm_03_loc_tag.child[0]";
connectAttr "lt_arm_03_loc_tag.prep" "lt_hand_01_loc_tag.prep";
connectAttr "lt_hand_02_loc_tag.pare" "lt_hand_01_loc_tag.child[0]";
connectAttr "lt_hand_01_loc_tag.prep" "lt_hand_02_loc_tag.prep";
connectAttr "lt_thumb_01_pivot_loc_tag.pare" "lt_hand_02_loc_tag.child[0]";
connectAttr "lt_index_01_loc_tag.pare" "lt_hand_02_loc_tag.child[1]";
connectAttr "lt_middle_01_loc_tag.pare" "lt_hand_02_loc_tag.child[2]";
connectAttr "lt_ring_01_loc_tag.pare" "lt_hand_02_loc_tag.child[3]";
connectAttr "lt_pinky_01_loc_tag.pare" "lt_hand_02_loc_tag.child[4]";
connectAttr "lt_thumb_02_loc_tag.pare" "lt_thumb_01_pivot_loc_tag.child[0]";
connectAttr "lt_hand_02_loc_tag.prep" "lt_thumb_01_pivot_loc_tag.prep";
connectAttr "lt_thumb_03_loc_tag.pare" "lt_thumb_02_loc_tag.child[0]";
connectAttr "lt_thumb_01_pivot_loc_tag.prep" "lt_thumb_02_loc_tag.prep";
connectAttr "lt_thumb_04_loc_tag.pare" "lt_thumb_03_loc_tag.child[0]";
connectAttr "lt_thumb_02_loc_tag.prep" "lt_thumb_03_loc_tag.prep";
connectAttr "lt_thumb_05_loc_tag.pare" "lt_thumb_04_loc_tag.child[0]";
connectAttr "lt_thumb_03_loc_tag.prep" "lt_thumb_04_loc_tag.prep";
connectAttr "lt_thumb_04_loc_tag.prep" "lt_thumb_05_loc_tag.prep";
connectAttr "lt_middle_02_loc_tag.pare" "lt_middle_01_loc_tag.child[0]";
connectAttr "lt_hand_02_loc_tag.prep" "lt_middle_01_loc_tag.prep";
connectAttr "lt_middle_03_loc_tag.pare" "lt_middle_02_loc_tag.child[0]";
connectAttr "lt_middle_01_loc_tag.prep" "lt_middle_02_loc_tag.prep";
connectAttr "lt_middle_04_loc_tag.pare" "lt_middle_03_loc_tag.child[0]";
connectAttr "lt_middle_02_loc_tag.prep" "lt_middle_03_loc_tag.prep";
connectAttr "lt_middle_05_loc_tag.pare" "lt_middle_04_loc_tag.child[0]";
connectAttr "lt_middle_03_loc_tag.prep" "lt_middle_04_loc_tag.prep";
connectAttr "lt_middle_04_loc_tag.prep" "lt_middle_05_loc_tag.prep";
connectAttr "lt_ring_02_loc_tag.pare" "lt_ring_01_loc_tag.child[0]";
connectAttr "lt_hand_02_loc_tag.prep" "lt_ring_01_loc_tag.prep";
connectAttr "lt_ring_03_loc_tag.pare" "lt_ring_02_loc_tag.child[0]";
connectAttr "lt_ring_01_loc_tag.prep" "lt_ring_02_loc_tag.prep";
connectAttr "lt_ring_04_loc_tag.pare" "lt_ring_03_loc_tag.child[0]";
connectAttr "lt_ring_02_loc_tag.prep" "lt_ring_03_loc_tag.prep";
connectAttr "lt_ring_05_loc_tag.pare" "lt_ring_04_loc_tag.child[0]";
connectAttr "lt_ring_03_loc_tag.prep" "lt_ring_04_loc_tag.prep";
connectAttr "lt_ring_04_loc_tag.prep" "lt_ring_05_loc_tag.prep";
connectAttr "lt_pinky_02_loc_tag.pare" "lt_pinky_01_loc_tag.child[0]";
connectAttr "lt_hand_02_loc_tag.prep" "lt_pinky_01_loc_tag.prep";
connectAttr "lt_pinky_03_loc_tag.pare" "lt_pinky_02_loc_tag.child[0]";
connectAttr "lt_pinky_01_loc_tag.prep" "lt_pinky_02_loc_tag.prep";
connectAttr "lt_pinky_04_loc_tag.pare" "lt_pinky_03_loc_tag.child[0]";
connectAttr "lt_pinky_02_loc_tag.prep" "lt_pinky_03_loc_tag.prep";
connectAttr "lt_pinky_05_loc_tag.pare" "lt_pinky_04_loc_tag.child[0]";
connectAttr "lt_pinky_03_loc_tag.prep" "lt_pinky_04_loc_tag.prep";
connectAttr "lt_pinky_04_loc_tag.prep" "lt_pinky_05_loc_tag.prep";
connectAttr "lt_index_02_loc_tag.pare" "lt_index_01_loc_tag.child[0]";
connectAttr "lt_hand_02_loc_tag.prep" "lt_index_01_loc_tag.prep";
connectAttr "lt_index_03_loc_tag.pare" "lt_index_02_loc_tag.child[0]";
connectAttr "lt_index_01_loc_tag.prep" "lt_index_02_loc_tag.prep";
connectAttr "lt_index_04_loc_tag.pare" "lt_index_03_loc_tag.child[0]";
connectAttr "lt_index_02_loc_tag.prep" "lt_index_03_loc_tag.prep";
connectAttr "lt_index_05_loc_tag.pare" "lt_index_04_loc_tag.child[0]";
connectAttr "lt_index_03_loc_tag.prep" "lt_index_04_loc_tag.prep";
connectAttr "lt_index_04_loc_tag.prep" "lt_index_05_loc_tag.prep";
connectAttr "lt_leg_04_fk_icon.msg" "lt_leg_04_fk_icon_tag.act";
connectAttr "lt_leg_03_fk_icon_tag.prep" "lt_leg_04_fk_icon_tag.prep";
connectAttr "lt_leg_02_fk_icon_tag.prep" "lt_leg_03_fk_icon_tag.prep";
connectAttr "lt_leg_03_fk_icon.msg" "lt_leg_03_fk_icon_tag.act";
connectAttr "lt_leg_04_fk_icon_tag.pare" "lt_leg_03_fk_icon_tag.child[0]";
connectAttr "lt_leg_01_fk_icon_tag.prep" "lt_leg_02_fk_icon_tag.prep";
connectAttr "lt_leg_02_fk_icon.msg" "lt_leg_02_fk_icon_tag.act";
connectAttr "lt_leg_03_fk_icon_tag.pare" "lt_leg_02_fk_icon_tag.child[0]";
connectAttr "ct_hip_icon_tag.prep" "lt_leg_01_fk_icon_tag.prep";
connectAttr "lt_leg_01_fk_icon.msg" "lt_leg_01_fk_icon_tag.act";
connectAttr "lt_leg_02_fk_icon_tag.pare" "lt_leg_01_fk_icon_tag.child[0]";
connectAttr "ct_hip_icon.msg" "ct_hip_icon_tag.act";
connectAttr "lt_leg_01_fk_icon_tag.pare" "ct_hip_icon_tag.child[0]";
connectAttr "makeNurbCircle8.oc" "transformGeometry22.ig";
connectAttr "makeNurbCircle9.oc" "transformGeometry23.ig";
connectAttr "transformGeometry23.og" "transformGeometry24.ig";
connectAttr "makeNurbCircle10.oc" "transformGeometry25.ig";
connectAttr "transformGeometry25.og" "transformGeometry26.ig";
connectAttr "makeNurbCircle11.oc" "transformGeometry27.ig";
connectAttr "transformGeometry27.og" "transformGeometry28.ig";
connectAttr "makeNurbCircle12.oc" "transformGeometry29.ig";
connectAttr "makeNurbCircle13.oc" "transformGeometry30.ig";
connectAttr "transformGeometry29.og" "transformGeometry31.ig";
connectAttr "transformGeometry30.og" "transformGeometry32.ig";
connectAttr "makeNurbCircle14.oc" "transformGeometry33.ig";
connectAttr "transformGeometry33.og" "transformGeometry34.ig";
connectAttr "makeNurbCircle15.oc" "transformGeometry35.ig";
connectAttr "transformGeometry35.og" "transformGeometry36.ig";
connectAttr "makeNurbCircle16.oc" "transformGeometry37.ig";
connectAttr "makeNurbCircle17.oc" "transformGeometry38.ig";
connectAttr "makeNurbCircle18.oc" "transformGeometry39.ig";
connectAttr "makeNurbCircle19.oc" "transformGeometry40.ig";
connectAttr "makeNurbCircle20.oc" "transformGeometry41.ig";
connectAttr "transformGeometry41.og" "transformGeometry42.ig";
connectAttr "transformGeometry37.og" "transformGeometry43.ig";
connectAttr "transformGeometry38.og" "transformGeometry44.ig";
connectAttr "transformGeometry39.og" "transformGeometry45.ig";
connectAttr "transformGeometry40.og" "transformGeometry46.ig";
connectAttr "transformGeometry42.og" "transformGeometry47.ig";
connectAttr "transformGeometry43.og" "transformGeometry48.ig";
connectAttr "transformGeometry44.og" "transformGeometry49.ig";
connectAttr "transformGeometry45.og" "transformGeometry50.ig";
connectAttr "transformGeometry46.og" "transformGeometry51.ig";
connectAttr "transformGeometry47.og" "transformGeometry52.ig";
connectAttr "transformGeometry19.og" "transformGeometry53.ig";
connectAttr "transformGeometry20.og" "transformGeometry54.ig";
connectAttr "transformGeometry21.og" "transformGeometry55.ig";
connectAttr "transformGeometry18.og" "transformGeometry56.ig";
connectAttr "transformGeometry48.og" "transformGeometry57.ig";
connectAttr "transformGeometry49.og" "transformGeometry58.ig";
connectAttr "transformGeometry50.og" "transformGeometry59.ig";
connectAttr "transformGeometry51.og" "transformGeometry60.ig";
connectAttr "transformGeometry52.og" "transformGeometry61.ig";
connectAttr "transformGeometry28.og" "transformGeometry62.ig";
connectAttr "transformGeometry57.og" "transformGeometry63.ig";
connectAttr "transformGeometry58.og" "transformGeometry64.ig";
connectAttr "transformGeometry59.og" "transformGeometry65.ig";
connectAttr "transformGeometry60.og" "transformGeometry66.ig";
connectAttr "transformGeometry61.og" "transformGeometry67.ig";
connectAttr "transformGeometry24.og" "transformGeometry68.ig";
connectAttr "transformGeometry68.og" "transformGeometry69.ig";
connectAttr "biped_lt_leg_01_loc_tag.pare" "biped_ct_hip_loc_tag.child[0]";
connectAttr "biped_ct_back_01_loc_tag.pare" "biped_ct_hip_loc_tag.child[1]";
connectAttr "biped_lt_leg_02_loc_tag.pare" "biped_lt_leg_01_loc_tag.child[0]";
connectAttr "biped_ct_hip_loc_tag.prep" "biped_lt_leg_01_loc_tag.prep";
connectAttr "biped_lt_leg_03_loc_tag.pare" "biped_lt_leg_02_loc_tag.child[0]";
connectAttr "biped_lt_leg_01_loc_tag.prep" "biped_lt_leg_02_loc_tag.prep";
connectAttr "biped_lt_leg_04_loc_tag.pare" "biped_lt_leg_03_loc_tag.child[0]";
connectAttr "biped_lt_leg_02_loc_tag.prep" "biped_lt_leg_03_loc_tag.prep";
connectAttr "biped_lt_toeA_01_loc_tag.pare" "biped_lt_leg_04_loc_tag.child[0]";
connectAttr "biped_lt_toeB_01_loc_tag.pare" "biped_lt_leg_04_loc_tag.child[1]";
connectAttr "biped_lt_toeC_01_loc_tag.pare" "biped_lt_leg_04_loc_tag.child[2]";
connectAttr "biped_lt_toeD_01_loc_tag.pare" "biped_lt_leg_04_loc_tag.child[3]";
connectAttr "biped_lt_toeE_01_loc_tag.pare" "biped_lt_leg_04_loc_tag.child[4]";
connectAttr "biped_lt_leg_03_loc_tag.prep" "biped_lt_leg_04_loc_tag.prep";
connectAttr "biped_lt_toeA_02_loc_tag.pare" "biped_lt_toeA_01_loc_tag.child[0]";
connectAttr "biped_lt_leg_04_loc_tag.prep" "biped_lt_toeA_01_loc_tag.prep";
connectAttr "biped_lt_toeA_03_loc_tag.pare" "biped_lt_toeA_02_loc_tag.child[0]";
connectAttr "biped_lt_toeA_01_loc_tag.prep" "biped_lt_toeA_02_loc_tag.prep";
connectAttr "biped_lt_toeA_02_loc_tag.prep" "biped_lt_toeA_03_loc_tag.prep";
connectAttr "biped_lt_toeB_02_loc_tag.pare" "biped_lt_toeB_01_loc_tag.child[0]";
connectAttr "biped_lt_leg_04_loc_tag.prep" "biped_lt_toeB_01_loc_tag.prep";
connectAttr "biped_lt_toeB_03_loc_tag.pare" "biped_lt_toeB_02_loc_tag.child[0]";
connectAttr "biped_lt_toeB_01_loc_tag.prep" "biped_lt_toeB_02_loc_tag.prep";
connectAttr "biped_lt_toeB_02_loc_tag.prep" "biped_lt_toeB_03_loc_tag.prep";
connectAttr "biped_lt_toeC_02_loc_tag.pare" "biped_lt_toeC_01_loc_tag.child[0]";
connectAttr "biped_lt_leg_04_loc_tag.prep" "biped_lt_toeC_01_loc_tag.prep";
connectAttr "biped_lt_toeC_03_loc_tag.pare" "biped_lt_toeC_02_loc_tag.child[0]";
connectAttr "biped_lt_toeC_01_loc_tag.prep" "biped_lt_toeC_02_loc_tag.prep";
connectAttr "biped_lt_toeC_02_loc_tag.prep" "biped_lt_toeC_03_loc_tag.prep";
connectAttr "biped_lt_toeD_02_loc_tag.pare" "biped_lt_toeD_01_loc_tag.child[0]";
connectAttr "biped_lt_leg_04_loc_tag.prep" "biped_lt_toeD_01_loc_tag.prep";
connectAttr "biped_lt_toeD_03_loc_tag.pare" "biped_lt_toeD_02_loc_tag.child[0]";
connectAttr "biped_lt_toeD_01_loc_tag.prep" "biped_lt_toeD_02_loc_tag.prep";
connectAttr "biped_lt_toeD_02_loc_tag.prep" "biped_lt_toeD_03_loc_tag.prep";
connectAttr "biped_lt_toeE_02_loc_tag.pare" "biped_lt_toeE_01_loc_tag.child[0]";
connectAttr "biped_lt_leg_04_loc_tag.prep" "biped_lt_toeE_01_loc_tag.prep";
connectAttr "biped_lt_toeE_03_loc_tag.pare" "biped_lt_toeE_02_loc_tag.child[0]";
connectAttr "biped_lt_toeE_01_loc_tag.prep" "biped_lt_toeE_02_loc_tag.prep";
connectAttr "biped_lt_toeE_02_loc_tag.prep" "biped_lt_toeE_03_loc_tag.prep";
connectAttr "biped_ct_hip_loc_tag.prep" "biped_ct_back_01_loc_tag.prep";
connectAttr "biped_ct_back_02_loc_tag.pare" "biped_ct_back_01_loc_tag.child[0]";
connectAttr "biped_ct_back_01_loc_tag.prep" "biped_ct_back_02_loc_tag.prep";
connectAttr "biped_ct_back_03_loc_tag.pare" "biped_ct_back_02_loc_tag.child[0]";
connectAttr "biped_ct_back_02_loc_tag.prep" "biped_ct_back_03_loc_tag.prep";
connectAttr "biped_ct_back_04_loc_tag.pare" "biped_ct_back_03_loc_tag.child[0]";
connectAttr "biped_ct_back_03_loc_tag.prep" "biped_ct_back_04_loc_tag.prep";
connectAttr "biped_ct_back_05_loc_tag.pare" "biped_ct_back_04_loc_tag.child[0]";
connectAttr "biped_ct_back_04_loc_tag.prep" "biped_ct_back_05_loc_tag.prep";
connectAttr "biped_ct_back_06_loc_tag.pare" "biped_ct_back_05_loc_tag.child[0]";
connectAttr "biped_lt_clav_01_loc_tag.pare" "biped_ct_back_05_loc_tag.child[1]";
connectAttr "biped_ct_back_05_loc_tag.prep" "biped_ct_back_06_loc_tag.prep";
connectAttr "biped_ct_back_07_loc_tag.pare" "biped_ct_back_06_loc_tag.child[0]";
connectAttr "biped_ct_back_06_loc_tag.prep" "biped_ct_back_07_loc_tag.prep";
connectAttr "biped_ct_neck_01_loc_tag.pare" "biped_ct_back_07_loc_tag.child[0]";
connectAttr "biped_ct_back_07_loc_tag.prep" "biped_ct_neck_01_loc_tag.prep";
connectAttr "biped_ct_neck_02_loc_tag.pare" "biped_ct_neck_01_loc_tag.child[0]";
connectAttr "biped_ct_neck_01_loc_tag.prep" "biped_ct_neck_02_loc_tag.prep";
connectAttr "biped_ct_neck_03_loc_tag.pare" "biped_ct_neck_02_loc_tag.child[0]";
connectAttr "biped_ct_neck_02_loc_tag.prep" "biped_ct_neck_03_loc_tag.prep";
connectAttr "biped_ct_neck_04_loc_tag.pare" "biped_ct_neck_03_loc_tag.child[0]";
connectAttr "biped_ct_neck_03_loc_tag.prep" "biped_ct_neck_04_loc_tag.prep";
connectAttr "biped_ct_head_01_loc_tag.pare" "biped_ct_neck_04_loc_tag.child[0]";
connectAttr "biped_ct_neck_04_loc_tag.prep" "biped_ct_head_01_loc_tag.prep";
connectAttr "biped_ct_head_02_loc_tag.pare" "biped_ct_head_01_loc_tag.child[0]";
connectAttr "biped_ct_jaw_01_loc_tag.pare" "biped_ct_head_01_loc_tag.child[1]";
connectAttr "biped_lt_eye_01_loc_tag.pare" "biped_ct_head_01_loc_tag.child[2]";
connectAttr "biped_ct_head_01_loc_tag.prep" "biped_ct_head_02_loc_tag.prep";
connectAttr "biped_ct_head_01_loc_tag.prep" "biped_lt_eye_01_loc_tag.prep";
connectAttr "biped_lt_eye_02_loc_tag.pare" "biped_lt_eye_01_loc_tag.child[0]";
connectAttr "biped_lt_eye_01_loc_tag.prep" "biped_lt_eye_02_loc_tag.prep";
connectAttr "biped_ct_head_01_loc_tag.prep" "biped_ct_jaw_01_loc_tag.prep";
connectAttr "biped_ct_jaw_02_loc_tag.pare" "biped_ct_jaw_01_loc_tag.child[0]";
connectAttr "biped_ct_jaw_01_loc_tag.prep" "biped_ct_jaw_02_loc_tag.prep";
connectAttr "biped_ct_back_05_loc_tag.prep" "biped_lt_clav_01_loc_tag.prep";
connectAttr "biped_lt_clav_02_loc_tag.pare" "biped_lt_clav_01_loc_tag.child[0]";
connectAttr "biped_lt_clav_01_loc_tag.prep" "biped_lt_clav_02_loc_tag.prep";
connectAttr "biped_lt_arm_01_loc_tag.pare" "biped_lt_clav_02_loc_tag.child[0]";
connectAttr "biped_lt_clav_02_loc_tag.prep" "biped_lt_arm_01_loc_tag.prep";
connectAttr "biped_lt_arm_02_loc_tag.pare" "biped_lt_arm_01_loc_tag.child[0]";
connectAttr "biped_lt_arm_01_loc_tag.prep" "biped_lt_arm_02_loc_tag.prep";
connectAttr "biped_lt_arm_03_loc_tag.pare" "biped_lt_arm_02_loc_tag.child[0]";
connectAttr "biped_lt_arm_02_loc_tag.prep" "biped_lt_arm_03_loc_tag.prep";
connectAttr "biped_lt_hand_01_loc_tag.pare" "biped_lt_arm_03_loc_tag.child[0]";
connectAttr "biped_lt_arm_03_loc_tag.prep" "biped_lt_hand_01_loc_tag.prep";
connectAttr "biped_lt_hand_02_loc_tag.pare" "biped_lt_hand_01_loc_tag.child[0]";
connectAttr "biped_lt_hand_01_loc_tag.prep" "biped_lt_hand_02_loc_tag.prep";
connectAttr "biped_lt_thumb_01_pivot_loc_tag.pare" "biped_lt_hand_02_loc_tag.child[0]"
		;
connectAttr "biped_lt_index_01_loc_tag.pare" "biped_lt_hand_02_loc_tag.child[1]"
		;
connectAttr "biped_lt_middle_01_loc_tag.pare" "biped_lt_hand_02_loc_tag.child[2]"
		;
connectAttr "biped_lt_ring_01_loc_tag.pare" "biped_lt_hand_02_loc_tag.child[3]";
connectAttr "biped_lt_pinky_01_loc_tag.pare" "biped_lt_hand_02_loc_tag.child[4]"
		;
connectAttr "biped_lt_thumb_02_loc_tag.pare" "biped_lt_thumb_01_pivot_loc_tag.child[0]"
		;
connectAttr "biped_lt_hand_02_loc_tag.prep" "biped_lt_thumb_01_pivot_loc_tag.prep"
		;
connectAttr "biped_lt_thumb_03_loc_tag.pare" "biped_lt_thumb_02_loc_tag.child[0]"
		;
connectAttr "biped_lt_thumb_01_pivot_loc_tag.prep" "biped_lt_thumb_02_loc_tag.prep"
		;
connectAttr "biped_lt_thumb_04_loc_tag.pare" "biped_lt_thumb_03_loc_tag.child[0]"
		;
connectAttr "biped_lt_thumb_02_loc_tag.prep" "biped_lt_thumb_03_loc_tag.prep";
connectAttr "biped_lt_thumb_05_loc_tag.pare" "biped_lt_thumb_04_loc_tag.child[0]"
		;
connectAttr "biped_lt_thumb_03_loc_tag.prep" "biped_lt_thumb_04_loc_tag.prep";
connectAttr "biped_lt_thumb_04_loc_tag.prep" "biped_lt_thumb_05_loc_tag.prep";
connectAttr "biped_lt_middle_02_loc_tag.pare" "biped_lt_middle_01_loc_tag.child[0]"
		;
connectAttr "biped_lt_hand_02_loc_tag.prep" "biped_lt_middle_01_loc_tag.prep";
connectAttr "biped_lt_middle_03_loc_tag.pare" "biped_lt_middle_02_loc_tag.child[0]"
		;
connectAttr "biped_lt_middle_01_loc_tag.prep" "biped_lt_middle_02_loc_tag.prep";
connectAttr "biped_lt_middle_04_loc_tag.pare" "biped_lt_middle_03_loc_tag.child[0]"
		;
connectAttr "biped_lt_middle_02_loc_tag.prep" "biped_lt_middle_03_loc_tag.prep";
connectAttr "biped_lt_middle_05_loc_tag.pare" "biped_lt_middle_04_loc_tag.child[0]"
		;
connectAttr "biped_lt_middle_03_loc_tag.prep" "biped_lt_middle_04_loc_tag.prep";
connectAttr "biped_lt_middle_04_loc_tag.prep" "biped_lt_middle_05_loc_tag.prep";
connectAttr "biped_lt_ring_02_loc_tag.pare" "biped_lt_ring_01_loc_tag.child[0]";
connectAttr "biped_lt_hand_02_loc_tag.prep" "biped_lt_ring_01_loc_tag.prep";
connectAttr "biped_lt_ring_03_loc_tag.pare" "biped_lt_ring_02_loc_tag.child[0]";
connectAttr "biped_lt_ring_01_loc_tag.prep" "biped_lt_ring_02_loc_tag.prep";
connectAttr "biped_lt_ring_04_loc_tag.pare" "biped_lt_ring_03_loc_tag.child[0]";
connectAttr "biped_lt_ring_02_loc_tag.prep" "biped_lt_ring_03_loc_tag.prep";
connectAttr "biped_lt_ring_05_loc_tag.pare" "biped_lt_ring_04_loc_tag.child[0]";
connectAttr "biped_lt_ring_03_loc_tag.prep" "biped_lt_ring_04_loc_tag.prep";
connectAttr "biped_lt_ring_04_loc_tag.prep" "biped_lt_ring_05_loc_tag.prep";
connectAttr "biped_lt_pinky_02_loc_tag.pare" "biped_lt_pinky_01_loc_tag.child[0]"
		;
connectAttr "biped_lt_hand_02_loc_tag.prep" "biped_lt_pinky_01_loc_tag.prep";
connectAttr "biped_lt_pinky_03_loc_tag.pare" "biped_lt_pinky_02_loc_tag.child[0]"
		;
connectAttr "biped_lt_pinky_01_loc_tag.prep" "biped_lt_pinky_02_loc_tag.prep";
connectAttr "biped_lt_pinky_04_loc_tag.pare" "biped_lt_pinky_03_loc_tag.child[0]"
		;
connectAttr "biped_lt_pinky_02_loc_tag.prep" "biped_lt_pinky_03_loc_tag.prep";
connectAttr "biped_lt_pinky_05_loc_tag.pare" "biped_lt_pinky_04_loc_tag.child[0]"
		;
connectAttr "biped_lt_pinky_03_loc_tag.prep" "biped_lt_pinky_04_loc_tag.prep";
connectAttr "biped_lt_pinky_04_loc_tag.prep" "biped_lt_pinky_05_loc_tag.prep";
connectAttr "biped_lt_index_02_loc_tag.pare" "biped_lt_index_01_loc_tag.child[0]"
		;
connectAttr "biped_lt_hand_02_loc_tag.prep" "biped_lt_index_01_loc_tag.prep";
connectAttr "biped_lt_index_03_loc_tag.pare" "biped_lt_index_02_loc_tag.child[0]"
		;
connectAttr "biped_lt_index_01_loc_tag.prep" "biped_lt_index_02_loc_tag.prep";
connectAttr "biped_lt_index_04_loc_tag.pare" "biped_lt_index_03_loc_tag.child[0]"
		;
connectAttr "biped_lt_index_02_loc_tag.prep" "biped_lt_index_03_loc_tag.prep";
connectAttr "biped_lt_index_05_loc_tag.pare" "biped_lt_index_04_loc_tag.child[0]"
		;
connectAttr "biped_lt_index_03_loc_tag.prep" "biped_lt_index_04_loc_tag.prep";
connectAttr "biped_lt_index_04_loc_tag.prep" "biped_lt_index_05_loc_tag.prep";
connectAttr "biped_lt_leg_03_fk_icon_tag.prep" "biped_lt_leg_04_fk_icon_tag.prep"
		;
connectAttr "biped_lt_leg_02_fk_icon_tag.prep" "biped_lt_leg_03_fk_icon_tag.prep"
		;
connectAttr "biped_lt_leg_04_fk_icon_tag.pare" "biped_lt_leg_03_fk_icon_tag.child[0]"
		;
connectAttr "biped_lt_leg_01_fk_icon_tag.prep" "biped_lt_leg_02_fk_icon_tag.prep"
		;
connectAttr "biped_lt_leg_03_fk_icon_tag.pare" "biped_lt_leg_02_fk_icon_tag.child[0]"
		;
connectAttr "biped_ct_hip_icon_tag.prep" "biped_lt_leg_01_fk_icon_tag.prep";
connectAttr "biped_lt_leg_02_fk_icon_tag.pare" "biped_lt_leg_01_fk_icon_tag.child[0]"
		;
connectAttr "biped_lt_leg_01_fk_icon_tag.pare" "biped_ct_hip_icon_tag.child[0]";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr ":rmanGlobals.msg" ":defaultRenderingList1.r" -na;
connectAttr ":PxrPathTracer.msg" ":defaultRenderingList1.r" -na;
// End of biped.ma
