

  //let staList = ['FL','NL', 'FL0', 'FL4G', 'FL60', 'FL330', 'FL660', 'FL1K'];
  let allstaList = ['FR', 'NR', 'NL', 'FL']

  let allchanList = ['HNX', 'HNY', 'HNZ'];

let loadSeismograms = function(timeWindow, staList=allstaList, chanList=allchanList) {
  let protocol = 'http:';
  if ("https:" == document.location.protocol) {
    protocol = 'https:'
  }
//  const host = document.location.hostname;
  const host = 'www.seis.sc.edu';
  let subdir = ""
  if (host === 'www.seis.sc.edu') {
    subdir = "dragrace";
  }
  let mseedQ = new seisplotjs.mseedarchive.MSeedArchive(
    `${protocol}//${host}/${subdir}`,
    "%n/%s/%Y/%j/%n.%s.%l.%c.%Y.%j.%H");

  let net = new seisplotjs.stationxml.Network("XX");
  let LOC = "00";
  let chanTR = [];
  for (let sta of staList) {
    let staObj = new seisplotjs.stationxml.Station(net, sta);
    for (let chan of chanList) {
      let chanObj = new seisplotjs.stationxml.Channel(staObj, chan, LOC);
      chanTR.push(seisplotjs.seismogram.SeismogramDisplayData.fromChannelAndTimeWindow(
            chanObj, timeWindow));
      console.log(`load ${sta} ${chan}`)
    }
  }
  return mseedQ.loadSeismograms(chanTR);
};
