<template>
<div class="center">
  <div class="container">


    <div class="row">
      <div class="col-sm-12 ">
       <h1 class="text-center">Your Trackers</h1>
        <hr><br>

        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col">Add Data</th>
              <th scope="col">Options</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(tracker, index) in trkrs" :key="index">
              <td>{{tracker.title}}</td>
              <td>{{tracker.genre}}</td>
              <td><button class="badge badge-success" v-b-modal.value-modal>+</button></td>
              <td>
                <div class="btn-group" role="group">
                <button type="button" class="btn btn-outline-dark btn-sm" v-b-modal.trkr-view-modal>View</button>
                <button type="button" class="btn btn-outline-dark btn-sm" v-b-modal.trkr-update-modal @click="editTrkr(tracker)">Update</button>
                <button type="button" class="btn btn-outline-dark btn-sm" @click="deleteTrkr(tracker)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <br><br>
        <button type="button" class="btn btn-danger btn-sm" v-b-modal.trkr-modal>Add Tracker</button>
      </div>
    </div>



    <b-modal size="xl" ref="addTrkrModal" id="trkr-modal" title="Add a new Tracker" hide-backdrop centered hide-footer no-fade>
    <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group" label="Name of the tracker:" label-for="form-title-input">
      <b-form-input id="form-title-input" type="text" v-model="addTrkrForm.title" required placeholder="Enter name"></b-form-input>
      </b-form-group>

      <b-form-group id="form-genre-group" label="Description of the tracker:" label-for="form-genre-input">
      <b-form-input id="form-genre-input" type="text" v-model="addTrkrForm.genre" required placeholder="Enter description"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
    </b-modal>



  <b-modal size="xl" ref="viewTrkrModal" id="trkr-view-modal" title="View Tracker" hide-backdrop centered hide-footer no-fade>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
    This is you tracker trends
    <br>
    <br>
    <b-button type="submit" variant="outline-info">Mail it to me</b-button>
    <b-button type="reset" variant="outline-danger">Download Tracker</b-button>
  </b-form>
  </b-modal>




    <b-modal size="xl" ref="addvalueModal" id="value-modal" title="Add Value" hide-backdrop centered hide-footer no-fade>
    <b-form @submit="onSubmitValue" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group" label="Tracking Date:" label-for="form-title-input">
      <b-form-input id="form-title-input" type="text" v-model="addTrkrForm.title" required placeholder="Enter name"></b-form-input>
      </b-form-group>

      <b-form-group id="form-genre-group" label="Description of the tracker:" label-for="form-genre-input">
      <b-form-input id="form-genre-input" type="text" v-model="addTrkrForm.genre" required placeholder="Enter description"></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="outline-info">Submit</b-button>
      <b-button type="reset" variant="outline-danger">Reset</b-button>
    </b-form>
    </b-modal>



  <b-modal size="xl" ref="editTrkrModal" id="trkr-update-modal" title="Update" hide-backdrop hide-footer centered no-fade>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      
    <b-form-group id="form-title-edit-group" label="Name:" label-for="form-title-edit-input">
    <b-form-input id="form-title-edit-input" type="text" v-model="editForm.title" required placeholder="Enter new Name"></b-form-input>
    </b-form-group>

    <b-form-group id="form-genre-edit-group" label="Description:" label-for="form-genre-edit-input">
    <b-form-input id="form-genre-edit-input" type="text" v-model="editForm.genre" placeholder="Enter new Description"></b-form-input>
    </b-form-group>

    <b-button-group>
      <b-button type="submit" variant="outline-info">Update</b-button>
      <b-button type="reset" variant="outline-danger">Cancel</b-button>
    </b-button-group>
  </b-form>
  </b-modal>




    <br>
    <br>
    <b-alert variant="light" v-if="showMessage" show> {{ message }} </b-alert>
  </div>
  </div>
</template>



<script>
import axios from 'axios';

export default {
  data() {
    return {
      trkrs: [],
      addTrkrForm: {
        title: '',
        genre: '',
      },
      editForm: {
      id: '',
      title: '',
      genre: '',
      },
    };
  },

  message:'',

methods: {
    getTrkrs() {
      const path = 'http://localhost:5000/trkrs';
      axios.get(path)
        .then((res) => {
          this.trkrs = res.data.trkrs;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    addTrkr(dataone) {
      const path = 'http://localhost:5000/trkrs';
      axios.post(path, dataone)
        .then(() => {
          this.getTrkrs();
          this.message = 'Tracker added!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getTrkrs();
        });
    },

     emptyform() {
        this.addTrkrForm.title = '';
        this.addTrkrForm.genre = '';
        this.editForm.id = '';
        this.editForm.title = '';
        this.editForm.genre = '';
      }, 

    onSubmit(e) {
      e.preventDefault();
      this.$refs.addvalueModal.hide();
      let played = false;
      if (this.addTrkrForm.played[0]) played = true;
      const dataone = {
        title: this.addTrkrForm.title,
        genre: this.addTrkrForm.genre,
        played, 
      };
      // this.addTrkr(dataone);
      this.emptyform();
    },




    onSubmitValue(e) {
      e.preventDefault();
      this.$refs.addTrkrModal.hide();
      let played = false;
      if (this.addTrkrForm.played[0]) played = true;
      const dataone = {
        title: this.addTrkrForm.title,
        genre: this.addTrkrForm.genre,
        played, 
      };
      this.addTrkr(dataone);
      this.emptyform();
    },



    onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editTrkrModal.hide();
    let played = false;
    if (this.editForm.played[0]) played = true;
    const dataone = {
      title: this.editForm.title,
      genre: this.editForm.genre,
      played,
    };
    this.updateTrkr(dataone, this.editForm.id);
  },

    onReset(e) {
      e.preventDefault();
      this.$refs.addTrkrModal.hide();
      this.emptyform();
    },

updateTrkr(dataone, trkrid) {
  const path = `http://localhost:5000/trkrs/${trkrid}`;
  axios.put(path, dataone)    
    .then(() => {
      this.getTrkrs();
      this.message = 'Tracker updated!';
      this.showMessage =  true;
    })
    .catch((error) => {
      console.error(error);
      this.getTrkrs();
    });
},

editTrkr(trkr) {
  this.editForm = trkr;
},

onResetUpdate(e) {
  e.preventDefault();
  this.$refs.editTrkrModal.hide();
  this.emptyform();
  this.getTrkrs(); 
},

removeTrkr(trkrid) {
  const path = `http://localhost:5000/trkrs/${trkrid}`;
  axios.delete(path)
    .then(() => {
      this.getTrkrs();
      this.message = 'Tracker Deleted!';
      this.showMessage = true;
    })
    .catch((error) => {
      console.error(error);
      this.getTrkrs();
    });
},
deleteTrkr(trkr) {
  this.removeTrkr(trkr.id);
},

  },
  created() {
    this.getTrkrs(); 
  },
};
</script>


<style>
#trkr-modal,#trkr-view-modal,#trkr-update-modal,#value-modal{
    background-color:white;
}
</style>