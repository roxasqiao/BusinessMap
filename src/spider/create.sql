CREATE COLUMN TABLE "CONFIG"."ZPOI_LAT_LNT" ("UID" NVARCHAR(50) NOT NULL ,
	 "BRAND_CODE" NVARCHAR(10),
	 "BRAND" NVARCHAR(50),
	 "NAME" VARCHAR(225),
	 "PROVINCE" VARCHAR(50),
	 "CITY" VARCHAR(225),
	 "AREA" VARCHAR(225),
	 "ADDRESS" VARCHAR(225),
	 "LAT" NVARCHAR(20),
	 "LNG" NVARCHAR(225),
	 "UPDAT" LONGDATE CS_LONGDATE,
	 "MORE01" VARCHAR(225) DEFAULT '',
	 "MORE02" VARCHAR(225) DEFAULT '',
	 "MORE03" VARCHAR(225) DEFAULT '',
	 "MORE04" VARCHAR(225) DEFAULT '',
	 "MORE05" VARCHAR(225) DEFAULT '',
	 "MORE06" VARCHAR(225) DEFAULT '',
	 PRIMARY KEY ("UID")) UNLOAD PRIORITY 5 AUTO MERGE 
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."UID" is 'poi的唯一标示，可用于详情检索 '
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."BRAND" is '品牌'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."NAME" is 'poi名称 '
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."PROVINCE" is '所属省份'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."CITY" is '所属城市'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."AREA" is '所属区县'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."ADDRESS" is '地址'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."LAT" is '纬度值'
;
COMMENT ON COLUMN "CONFIG"."ZPOI_LAT_LNT"."LNG" is '经度值'