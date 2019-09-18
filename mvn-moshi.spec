#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-moshi
Version  : 1.5.0
Release  : 1
URL      : https://github.com/square/moshi/archive/moshi-parent-1.5.0.tar.gz
Source0  : https://github.com/square/moshi/archive/moshi-parent-1.5.0.tar.gz
Source1  : https://repo1.maven.org/maven2/com/squareup/moshi/moshi-parent/1.5.0/moshi-parent-1.5.0.pom
Source2  : https://repo1.maven.org/maven2/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.jar
Source3  : https://repo1.maven.org/maven2/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-moshi-data = %{version}-%{release}
Requires: mvn-moshi-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
Moshi
=====
Moshi is a modern JSON library for Android and Java. It makes it easy to parse JSON into Java
objects:

%package data
Summary: data components for the mvn-moshi package.
Group: Data

%description data
data components for the mvn-moshi package.


%package license
Summary: license components for the mvn-moshi package.
Group: Default

%description license
license components for the mvn-moshi package.


%prep
%setup -q -n moshi-moshi-parent-1.5.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-moshi
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-moshi/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi-parent/1.5.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi-parent/1.5.0/moshi-parent-1.5.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/squareup/moshi/moshi-parent/1.5.0/moshi-parent-1.5.0.pom
/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.jar
/usr/share/java/.m2/repository/com/squareup/moshi/moshi/1.5.0/moshi-1.5.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-moshi/LICENSE.txt
