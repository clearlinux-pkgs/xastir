#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xastir
Version  : 208
Release  : 2
URL      : https://github.com/Xastir/Xastir/archive/xastir208.tar.gz
Source0  : https://github.com/Xastir/Xastir/archive/xastir208.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: xastir-bin
Requires: xastir-doc
Requires: xastir-data
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : curl-dev
BuildRequires : db-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : motif-dev
BuildRequires : pcre-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xt)
Patch1: 0001-configure.ac-don-t-remove-duplicates.patch

%description
$Id$
------------------------------------------------------------------------
Please at least SKIM this document before asking questions. In fact,
READ IT if you've never successfully set up Xastir before. PLEASE!
READ IT! If you haven't read this file, and ask for help

%package bin
Summary: bin components for the xastir package.
Group: Binaries
Requires: xastir-data

%description bin
bin components for the xastir package.


%package data
Summary: data components for the xastir package.
Group: Data

%description data
data components for the xastir package.


%package doc
Summary: doc components for the xastir package.
Group: Documentation

%description doc
doc components for the xastir package.


%prep
%setup -q -n Xastir-xastir208
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507855485
%reconfigure --disable-static --without-imagemagick
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1507855485
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/callpass
/usr/bin/testdbfawk
/usr/bin/xastir
/usr/bin/xastir_udp_client

%files data
%defattr(-,root,root,-)
/usr/share/xastir/Counties/placeholder
/usr/share/xastir/GNIS/placeholder
/usr/share/xastir/config/24kgrid.dbfawk
/usr/share/xastir/config/OSM_Cloudmade_administrative.dbfawk
/usr/share/xastir/config/OSM_Cloudmade_highway.dbfawk
/usr/share/xastir/config/OSM_Cloudmade_natural.dbfawk
/usr/share/xastir/config/OSM_Cloudmade_poi.dbfawk
/usr/share/xastir/config/OSM_Cloudmade_water_and_coastline.dbfawk
/usr/share/xastir/config/arealm.dbfawk
/usr/share/xastir/config/areawater.dbfawk
/usr/share/xastir/config/cousub.dbfawk
/usr/share/xastir/config/cousub00.dbfawk
/usr/share/xastir/config/edge.dbfawk
/usr/share/xastir/config/featnames.dbfawk
/usr/share/xastir/config/gfe_coastal_waters.dbfawk
/usr/share/xastir/config/gfe_coastal_waters_warnings.dbfawk
/usr/share/xastir/config/gfe_fire_weather.dbfawk
/usr/share/xastir/config/gfe_metro_areas.dbfawk
/usr/share/xastir/config/gfe_public_weather.dbfawk
/usr/share/xastir/config/gps_wpt.dbfawk
/usr/share/xastir/config/language-Dutch.sys
/usr/share/xastir/config/language-ElmerFudd.sys
/usr/share/xastir/config/language-English.sys
/usr/share/xastir/config/language-French.sys
/usr/share/xastir/config/language-German.sys
/usr/share/xastir/config/language-Italian.sys
/usr/share/xastir/config/language-MuppetsChef.sys
/usr/share/xastir/config/language-OldeEnglish.sys
/usr/share/xastir/config/language-PigLatin.sys
/usr/share/xastir/config/language-PirateEnglish.sys
/usr/share/xastir/config/language-Portuguese.sys
/usr/share/xastir/config/language-Spanish.sys
/usr/share/xastir/config/nwsc_ddmmyy.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_09.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_09b.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_10.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_10a.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_13.dbfawk
/usr/share/xastir/config/nwsc_ddmmyy_15.dbfawk
/usr/share/xastir/config/nwshzddmmyy.dbfawk
/usr/share/xastir/config/nwsmzddmmyy.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_09.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_11.dbfawk
/usr/share/xastir/config/nwsmzoddmmyy.dbfawk
/usr/share/xastir/config/nwsozddap12.dbfawk
/usr/share/xastir/config/nwsozddmmyy.dbfawk
/usr/share/xastir/config/nwsozddmmyy_09.dbfawk
/usr/share/xastir/config/nwsozddmmyy_14.dbfawk
/usr/share/xastir/config/nwsw_ddjn12.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_09.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_10.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_13.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_14.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_14a.dbfawk
/usr/share/xastir/config/nwsz1ddmmyy.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_09.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10b.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10c.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_11.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_13.dbfawk
/usr/share/xastir/config/nwszoddmmyy.dbfawk
/usr/share/xastir/config/pointlm.dbfawk
/usr/share/xastir/config/predefined_EVENT.sys
/usr/share/xastir/config/predefined_SAR.sys
/usr/share/xastir/config/stored_track.dbfawk
/usr/share/xastir/config/tabblock.dbfawk
/usr/share/xastir/config/tgr2shp.dbfawk
/usr/share/xastir/config/tgr2shppoly.dbfawk
/usr/share/xastir/config/tgr2shppoly_2006.dbfawk
/usr/share/xastir/config/tgrcty.dbfawk
/usr/share/xastir/config/tgrkgl.dbfawk
/usr/share/xastir/config/tgrlk.dbfawk
/usr/share/xastir/config/tgrlpt.dbfawk
/usr/share/xastir/config/tgrlpy.dbfawk
/usr/share/xastir/config/tgrplc00.dbfawk
/usr/share/xastir/config/tgrwat.dbfawk
/usr/share/xastir/config/tl_2009_aiannh.dbfawk
/usr/share/xastir/config/tl_2009_aits.dbfawk
/usr/share/xastir/config/tl_2009_arealm.dbfawk
/usr/share/xastir/config/tl_2009_areawater.dbfawk
/usr/share/xastir/config/tl_2009_county.dbfawk
/usr/share/xastir/config/tl_2009_cousub.dbfawk
/usr/share/xastir/config/tl_2009_edges.dbfawk
/usr/share/xastir/config/tl_2009_mil.dbfawk
/usr/share/xastir/config/tl_2009_nn_county.dbfawk
/usr/share/xastir/config/tl_2009_pointlm.dbfawk
/usr/share/xastir/config/tl_2009_zcta5.dbfawk
/usr/share/xastir/config/tnc-startup.aea
/usr/share/xastir/config/tnc-startup.d700
/usr/share/xastir/config/tnc-startup.d72_d710
/usr/share/xastir/config/tnc-startup.kam
/usr/share/xastir/config/tnc-startup.kpc2
/usr/share/xastir/config/tnc-startup.kpc3
/usr/share/xastir/config/tnc-startup.null
/usr/share/xastir/config/tnc-startup.paccomm
/usr/share/xastir/config/tnc-startup.pico
/usr/share/xastir/config/tnc-startup.sys
/usr/share/xastir/config/tnc-startup.thd7
/usr/share/xastir/config/tnc-startup.tnc2
/usr/share/xastir/config/tnc-startup.tnc2-ui
/usr/share/xastir/config/tnc-stop.d700
/usr/share/xastir/config/tnc-stop.d72_d710
/usr/share/xastir/config/tnc-stop.sys
/usr/share/xastir/config/tnc-stop.thd7
/usr/share/xastir/config/tnc-stop.tnc2-ui
/usr/share/xastir/config/xastir.rgb
/usr/share/xastir/fcc/placeholder
/usr/share/xastir/help/help-Dutch.dat
/usr/share/xastir/help/help-English.dat
/usr/share/xastir/help/help-French.dat
/usr/share/xastir/help/help-German.dat
/usr/share/xastir/help/help-Italian.dat
/usr/share/xastir/help/help-Portuguese.dat
/usr/share/xastir/help/help-Spanish.dat
/usr/share/xastir/maps/CC_OpenStreetMap.png
/usr/share/xastir/maps/CC_OpenStreetMap_logo.png
/usr/share/xastir/maps/CC_OpenStreetMap_txt.png
/usr/share/xastir/maps/GPS/placeholder
/usr/share/xastir/maps/Online/OSM_tiled_cycle.geo
/usr/share/xastir/maps/Online/OSM_tiled_fosm.geo
/usr/share/xastir/maps/Online/OSM_tiled_mapnik.geo
/usr/share/xastir/maps/Online/OSM_tiled_mapquest-aerial.geo
/usr/share/xastir/maps/Online/OSM_tiled_mapquest.geo
/usr/share/xastir/maps/worldhi.map
/usr/share/xastir/scripts/Coordinate.pm
/usr/share/xastir/scripts/Xastir_tigerpoly.py
/usr/share/xastir/scripts/ads-b.pl
/usr/share/xastir/scripts/ais.pl
/usr/share/xastir/scripts/ais_pp.pl
/usr/share/xastir/scripts/coord-convert.pl
/usr/share/xastir/scripts/geopdf2gtiff.pl
/usr/share/xastir/scripts/get-BOMdata
/usr/share/xastir/scripts/get-NWSdata
/usr/share/xastir/scripts/get-fcc-rac.pl
/usr/share/xastir/scripts/get-gnis
/usr/share/xastir/scripts/get-pop
/usr/share/xastir/scripts/gpx2shape
/usr/share/xastir/scripts/icontable.pl
/usr/share/xastir/scripts/inf2geo.pl
/usr/share/xastir/scripts/kiss-off.pl
/usr/share/xastir/scripts/langElmerFudd.pl
/usr/share/xastir/scripts/langMuppetsChef.pl
/usr/share/xastir/scripts/langOldeEnglish.pl
/usr/share/xastir/scripts/langPigLatin.pl
/usr/share/xastir/scripts/langPirateEnglish.pl
/usr/share/xastir/scripts/mapblast2geo.pl
/usr/share/xastir/scripts/mapfgd.pl
/usr/share/xastir/scripts/object2shp.pl
/usr/share/xastir/scripts/overlay.pl
/usr/share/xastir/scripts/ozi2geo.pl
/usr/share/xastir/scripts/permutations.pl
/usr/share/xastir/scripts/pos2shp.pl
/usr/share/xastir/scripts/ridge_radar.pl
/usr/share/xastir/scripts/slideshow.pl
/usr/share/xastir/scripts/split_gnis.bash
/usr/share/xastir/scripts/split_gnis.pl
/usr/share/xastir/scripts/test_coord.pl
/usr/share/xastir/scripts/toporama250k.pl
/usr/share/xastir/scripts/toporama50k.pl
/usr/share/xastir/scripts/track-get.pl
/usr/share/xastir/scripts/update_langfile.pl
/usr/share/xastir/scripts/values
/usr/share/xastir/scripts/values.pl
/usr/share/xastir/scripts/waypoint-get.pl
/usr/share/xastir/scripts/xastir-fixcfg.sh
/usr/share/xastir/scripts/xastir-migrate.sh
/usr/share/xastir/sounds/placeholder
/usr/share/xastir/symbols/13pct.xbm
/usr/share/xastir/symbols/25pct.xbm
/usr/share/xastir/symbols/2x2.xbm
/usr/share/xastir/symbols/alert.xbm
/usr/share/xastir/symbols/flood.xbm
/usr/share/xastir/symbols/icon.png
/usr/share/xastir/symbols/red_flag.xbm
/usr/share/xastir/symbols/snow.xbm
/usr/share/xastir/symbols/symbols.dat
/usr/share/xastir/symbols/torndo.xbm
/usr/share/xastir/symbols/wind.xbm
/usr/share/xastir/symbols/winter_storm.xbm
/usr/share/xastir/symbols/winter_weather.xbm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xastir/*
%doc /usr/share/man/man1/*
