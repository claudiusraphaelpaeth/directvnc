Summary:	DirectVNC - VNC client for DirectFB
Summary(pl):	DirectVNC - klient VNC dla DirectFB
Name:		directvnc
Version:	0.7.5
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	http://freesoftware.fsf.org/download/directvnc/%{name}-%{version}.tar.gz
# Source0-md5:	1fba84dc5450751bb402b68a9b9fb429
Patch0:		%{name}-caps.patch
Patch1:		%{name}-latin2.patch
Patch2:		%{name}-ctrl_alt_backspace.patch
URL:		http://www.adam-lilienthal.de/directvnc/
BuildRequires:	DirectFB-devel >= 0.9.24
BuildRequires:	XFree86-devel
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirectVNC is a client implementing the remote framebuffer protocol
(rfb) which is used by VNC servers. If a VNC server is running on a
machine you can connect to it using this client and have the contents
of its display shown on your screen. Keyboard and mouse events are
sent to the server, so you can basically control a VNC server
remotely. There are servers (and other clients) freely available for
all operating systems. What makes DirectVNC different from other unix
VNC clients is that it uses the linux framebuffer device through the
DirectFB library which enables it to run on anything that has a
framebuffer without the need for a running X server. This includes
embedded devices. DirectFB even uses acceleration features of certain
graphics cards.

%description -l pl
DirectVNC jest klientem zawieraj�cym implementacj� protoko�u zdalnego
framebuffera (rfb - remote framebuffer protocol), u�ywanego przez
serwery VNC. Je�li serwer VNC dzia�a na jakiej� maszynie, mo�na si�
z ni� po��czy� przy u�yciu tego klienta i widzie� zawarto�� jego
ekranu na swoim. Zdarzenia z klawiatury i myszy s� wysy�ane do
serwera, wi�c mo�na zdalnie kontrolowa� serwer VNC. Istniej� serwery
(i inne klienty) dost�pne za darmo na wiele system�w operacyjnych.
DirectFB od innych uniksowych klient�w VNC r�ni si� tym, �e u�ywa
linuksowego framebuffera poprzez bibliotek� DirectFB, co pozwala na
prac� bez potrzeby uruchamiania X serwera. Jednym z zastosowa� s�
urz�dzenia wbudowane. DirectFB mo�e nawet u�ywa� sprz�towej
akceleracji na niekt�rych kartach graficznych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
