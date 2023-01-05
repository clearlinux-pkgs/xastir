#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xastir
Version  : 2.1.8
Release  : 33
URL      : https://github.com/Xastir/Xastir/archive/Release-2.1.8/Xastir-2.1.8.tar.gz
Source0  : https://github.com/Xastir/Xastir/archive/Release-2.1.8/Xastir-2.1.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: xastir-bin = %{version}-%{release}
Requires: xastir-data = %{version}-%{release}
Requires: xastir-filemap = %{version}-%{release}
Requires: xastir-license = %{version}-%{release}
Requires: xastir-man = %{version}-%{release}
BuildRequires : ImageMagick
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : curl-dev
BuildRequires : gettext-bin
BuildRequires : libgeotiff-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : motif-dev
BuildRequires : pcre-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(MagickCore-7.Q16HDRI)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(proj)
BuildRequires : pkgconfig(shapelib)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xt)
Patch1: 0001-Add-stateless-support-in-var-lib-xastir.patch

%description
------------------------------------------------------------------------
Please at least SKIM this document before asking questions. In fact,
READ IT if you've never successfully set up Xastir before. PLEASE!
READ IT! If you haven't read this file, and ask for help

%package bin
Summary: bin components for the xastir package.
Group: Binaries
Requires: xastir-data = %{version}-%{release}
Requires: xastir-license = %{version}-%{release}
Requires: xastir-filemap = %{version}-%{release}

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
Requires: xastir-man = %{version}-%{release}

%description doc
doc components for the xastir package.


%package filemap
Summary: filemap components for the xastir package.
Group: Default

%description filemap
filemap components for the xastir package.


%package license
Summary: license components for the xastir package.
Group: Default

%description license
license components for the xastir package.


%package man
Summary: man components for the xastir package.
Group: Default

%description man
man components for the xastir package.


%prep
%setup -q -n Xastir-Release-2.1.8
cd %{_builddir}/Xastir-Release-2.1.8
%patch1 -p1
pushd ..
cp -a Xastir-Release-2.1.8 buildavx2
popd
pushd ..
cp -a Xastir-Release-2.1.8 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656343293
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656343293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xastir
cp %{_builddir}/Xastir-Release-2.1.8/COPYING %{buildroot}/usr/share/package-licenses/xastir/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/Xastir-Release-2.1.8/COPYING.LIB.LESSTIF %{buildroot}/usr/share/package-licenses/xastir/5fb362ef1680e635fe5fb212b55eef4db9ead48f
cp %{_builddir}/Xastir-Release-2.1.8/Davis/COPYING %{buildroot}/usr/share/package-licenses/xastir/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/Xastir-Release-2.1.8/LaCrosse/COPYING %{buildroot}/usr/share/package-licenses/xastir/74a8a6531a42e124df07ab5599aad63870fa0bd4
cp %{_builddir}/Xastir-Release-2.1.8/src/LICENSE.geocoder %{buildroot}/usr/share/package-licenses/xastir/963def3115497942492836e7a36d48b95f5a5fda
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/callpass
/usr/bin/testdbfawk
/usr/bin/xastir
/usr/bin/xastir_udp_client
/usr/share/clear/optimized-elf/bin*

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
/usr/share/xastir/config/OSM_geofabrik_roads.dbfawk
/usr/share/xastir/config/OSM_geofabrik_waterways.dbfawk
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
/usr/share/xastir/config/nwsfz_ddmmyy_19.dbfawk
/usr/share/xastir/config/nwshzddmmyy.dbfawk
/usr/share/xastir/config/nwshzddmmyy_old14.dbfawk
/usr/share/xastir/config/nwsmzddmmyy.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_09.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_11.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_16.dbfawk
/usr/share/xastir/config/nwsmzddmmyy_17.dbfawk
/usr/share/xastir/config/nwsmzoddmmyy.dbfawk
/usr/share/xastir/config/nwsozddap12.dbfawk
/usr/share/xastir/config/nwsozddmmyy.dbfawk
/usr/share/xastir/config/nwsozddmmyy_09.dbfawk
/usr/share/xastir/config/nwsozddmmyy_14.dbfawk
/usr/share/xastir/config/nwsozddmmyy_14b.dbfawk
/usr/share/xastir/config/nwsw_ddjn12.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_09.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_10.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_13.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_14.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_14a.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_17.dbfawk
/usr/share/xastir/config/nwsw_ddmmyy_20.dbfawk
/usr/share/xastir/config/nwsz1ddmmyy.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_09.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10b.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_10c.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_11.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_13.dbfawk
/usr/share/xastir/config/nwsz_ddmmyy_19.dbfawk
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
/usr/share/xastir/maps/Online/USTigermap.geo
/usr/share/xastir/maps/Online/USTigermapBorders.geo
/usr/share/xastir/maps/Online/geogratis.gc.ca/National.geo
/usr/share/xastir/maps/Online/geogratis.gc.ca/Regional.geo
/usr/share/xastir/maps/Online/geogratis.gc.ca/Sub_national.geo
/usr/share/xastir/maps/Online/geogratis.gc.ca/Sub_regional.geo
/usr/share/xastir/maps/Online/nationalmap.gov/WMS_USGS_Hydrography.geo
/usr/share/xastir/maps/Online/nationalmap.gov/WMS_USGS_ImageryOnly.geo
/usr/share/xastir/maps/Online/nationalmap.gov/WMS_USGS_ImageryTopo.geo
/usr/share/xastir/maps/Online/nationalmap.gov/WMS_USGS_ShadedReliefOnly.geo
/usr/share/xastir/maps/Online/nationalmap.gov/WMS_USGS_Topo.geo
/usr/share/xastir/maps/worldhi.map
/usr/share/xastir/scripts/Coordinate.pm
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
/usr/share/xastir/scripts/waypoint-get.pl
/usr/share/xastir/scripts/wms.pl
/usr/share/xastir/scripts/wxnowsrv.pl
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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xastir/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-xastir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xastir/5fb362ef1680e635fe5fb212b55eef4db9ead48f
/usr/share/package-licenses/xastir/74a8a6531a42e124df07ab5599aad63870fa0bd4
/usr/share/package-licenses/xastir/963def3115497942492836e7a36d48b95f5a5fda

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/callpass.1
/usr/share/man/man1/testdbfawk.1
/usr/share/man/man1/xastir.1
/usr/share/man/man1/xastir_udp_client.1
