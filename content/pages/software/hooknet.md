title: HookNet
template: project-single
picture: software/concept_hooknet2.png
description: HookNet: multi-resolution convolutional neural networks for semantic segmentation in histopathology whole-slide images
groups: pathology, diag
people: Mart van Rijthoven, Maschenka Balkenhol,  Jeroen van der Laak, Francesco Ciompi
openseadragon: true

1. [Online examples](#examples)
5. [More information](#info)

<figure class="figure my-4">
  <img data-src="/images/software/concept_hooknet2.png" class="figure-img img-fluid lazyload" alt="Example segmentations of Hooknet.">
  <figcaption class="figure-caption">Overview of the network architecture</figcaption>
</figure>

<a name="examples"></a>
## Online examples

The examples below show the output of HookNet, overlayed on the processed WSIs. You can zoom in by scrolling, moving around can be done with click&drag.

<div class="row my-4">
  <div class="col-md-6">
    <div id="openseadragon1" class="img-thumbnail" style="width: 100%; height: 400px;"></div>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch HookNet" onclick="switchHookNetdcis()"/>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch U-Net(0.5)" onclick="switchUnet05dcis()"/>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch U-Net(8.0)" onclick="switchUnet80dcis()"/>
  </div>
  <div class="col-md-6  ">
    <div id="openseadragon2" class="img-thumbnail" style="width: 100%; height: 400px;"></div>
    <input id="switch_ground_truth" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch ground truth" onclick="switchGroundTruthdcis()"/>
  </div>
</div>


<div class="row my-4">
  <div class="col-md-6">
    <div id="openseadragon3" class="img-thumbnail" style="width: 100%; height: 400px;"></div>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch HookNet" onclick="switchHookNetidc()"/>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch U-Net(0.5)" onclick="switchUnet05idc()"/>
    <input id="switch_prediction" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="switch U-Net(8.0)" onclick="switchUnet80idc()"/>
  </div>
  <div class="col-md-6  ">
    <div id="openseadragon4" class="img-thumbnail" style="width: 100%; height: 400px;"></div>
    <input id="switch_ground_truth" class="btn btn-secondary" style="height:25px;width:150px;font-size:10px;margin:5px;" type="button" value="show ground truth" onclick="switchGroundTruthidc()"/>
  </div>
</div>


Further questions regarding HookNet can be addressed to: [member/mart-van-rijthoven].

<script type="text/javascript">

function switchHookNetdcis(){
  viewer1.world.getItemAt(1).setOpacity(0.8);
  viewer1.world.getItemAt(2).setOpacity(0);
  viewer1.world.getItemAt(3).setOpacity(0);
}

function switchUnet05dcis(){
  viewer1.world.getItemAt(1).setOpacity(0);
  viewer1.world.getItemAt(2).setOpacity(0.8);
  viewer1.world.getItemAt(3).setOpacity(0);
}

function switchUnet80dcis(){
  viewer1.world.getItemAt(1).setOpacity(0);
  viewer1.world.getItemAt(2).setOpacity(0);
  viewer1.world.getItemAt(3).setOpacity(0.8);
}

function switchGroundTruthdcis(){
  viewer2.world.getItemAt(1).setOpacity((viewer2.world.getItemAt(1).getOpacity())?0:0.8);
}



viewer1Handler = function() {
  if (viewer2Leading) {
    return;
  }

  viewer1Leading = true;
  viewer2.viewport.zoomTo(viewer1.viewport.getZoom());
  viewer2.viewport.panTo(viewer1.viewport.getCenter());
  viewer1Leading = false;
};

viewer2Handler = function() {
  if (viewer1Leading) {
    return;
  }

  viewer2Leading = true;
  viewer1.viewport.zoomTo(viewer2.viewport.getZoom());
  viewer1.viewport.panTo(viewer2.viewport.getCenter());
  viewer2Leading = false;
};


viewer3Handler = function() {
  if (viewer4Leading) {
    return;
  }

  viewer3Leading = true;
  viewer4.viewport.zoomTo(viewer3.viewport.getZoom());
  viewer4.viewport.panTo(viewer3.viewport.getCenter());
  viewer3Leading = false;
};

viewer4Handler = function() {
  if (viewer3Leading) {
    return;
  }

  viewer4Leading = true;
  viewer3.viewport.zoomTo(viewer4.viewport.getZoom());
  viewer3.viewport.panTo(viewer4.viewport.getCenter());
  viewer4Leading = false;
};


function switchHookNetidc(){
  viewer3.world.getItemAt(1).setOpacity(0.8);
  viewer3.world.getItemAt(2).setOpacity(0);
  viewer3.world.getItemAt(3).setOpacity(0);
}

function switchUnet05idc(){
  viewer3.world.getItemAt(1).setOpacity(0);
  viewer3.world.getItemAt(2).setOpacity(0.8);
  viewer3.world.getItemAt(3).setOpacity(0);
}

function switchUnet80idc(){
  viewer3.world.getItemAt(1).setOpacity(0);
  viewer3.world.getItemAt(2).setOpacity(0);
  viewer3.world.getItemAt(3).setOpacity(0.8);
}

function switchGroundTruthidc(){
  viewer4.world.getItemAt(1).setOpacity((viewer4.world.getItemAt(1).getOpacity())?0:0.8);
}









function loadDzi() {
  viewer1 = OpenSeadragon({
      id: "openseadragon1",
      prefixUrl: "/dzi/images/",
      tileSources: "/dzi/hooknet/dcis/dcis_image_color.dzi"
     
  });

  viewer1.addTiledImage({
      tileSource: "/dzi/hooknet/dcis/dcis_hooknet_color.dzi",
      index: 1,
      opacity: 0.8
  });

  viewer1.addTiledImage({
      tileSource: "/dzi/hooknet/dcis/dcis_unet05_color.dzi",
      index: 2,
      opacity: 0.0
  });
  viewer1.addTiledImage({
      tileSource: "/dzi/hooknet/dcis/dcis_unet80_color.dzi",
      index: 3,
      opacity: 0.0
  });
 

  viewer2 = OpenSeadragon({
      id: "openseadragon2",
      prefixUrl: "/dzi/images/",
      tileSources: "/dzi/hooknet/dcis/dcis_image_color.dzi"
  });

  viewer2.addTiledImage({
      tileSource: "/dzi/hooknet/dcis/dcis_true_color.dzi",
      index: 1,
      opacity: 0.8
  });

viewer1Leading = false;
viewer2Leading = false;

viewer1.addHandler('zoom', viewer1Handler);
viewer2.addHandler('zoom', viewer2Handler);
viewer1.addHandler('pan', viewer1Handler);
viewer2.addHandler('pan', viewer2Handler);



viewer3 = OpenSeadragon({
      id: "openseadragon3",
      prefixUrl: "/dzi/images/",
      tileSources: "/dzi/hooknet/idc/idc_image_color.dzi"
     
  });

  viewer3.addTiledImage({
      tileSource: "/dzi/hooknet/idc/idc_hooknet_color.dzi",
      index: 1,
      opacity: 0.8
  });

  viewer3.addTiledImage({
      tileSource: "/dzi/hooknet/idc/idc_unet05_color.dzi",
      index: 2,
      opacity: 0.0
  });
  viewer3.addTiledImage({
      tileSource: "/dzi/hooknet/idc/idc_unet80_color.dzi",
      index: 3,
      opacity: 0.0
  });
 

  viewer4 = OpenSeadragon({
      id: "openseadragon4",
      prefixUrl: "/dzi/images/",
      tileSources: "/dzi/hooknet/idc/idc_image_color.dzi"
  });

  viewer4.addTiledImage({
      tileSource: "/dzi/hooknet/idc/idc_true_color.dzi",
      index: 1,
      opacity: 0.8
  });

viewer3Leading = false;
viewer4Leading = false;

viewer3.addHandler('zoom', viewer3Handler);
viewer4.addHandler('zoom', viewer4Handler);
viewer3.addHandler('pan', viewer3Handler);
viewer4.addHandler('pan', viewer4Handler);





}
</script>
